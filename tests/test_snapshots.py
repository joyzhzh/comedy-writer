#!/usr/bin/env python3
"""Exercise draft preservation and recovery, retaining all temporary artifacts."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / ".agents/skills/comedy-writer/scripts/snapshots.py"


def main():
    project = Path(tempfile.mkdtemp(prefix="comedy-writer-smoke-"))
    checks = []

    def run(*args, data=None, ok=True):
        result = subprocess.run(
            [sys.executable, str(HELPER), *map(str, args)],
            input=json.dumps(data, ensure_ascii=False) if data is not None else None,
            text=True, capture_output=True, cwd=ROOT,
        )
        assert (result.returncode == 0) == ok, result.stderr
        return result.stdout

    def save(data, *extra):
        path = Path(run("save", project, "--input", "-", *extra, data=data).strip())
        return path, json.loads(path.read_text())

    original = {
        "title": "Voice and recovery check", "stage": "input",
        "brief": {"facts": ["I labelled a drawer miscellaneous."],
                  "voice": "Quiet. Keep my pauses and British spelling."},
        "material": "  I labelled it ‘miscellaneous’.\n\nI’m still not sure.\n",
        "feedback": [], "revision_notes": [],
    }
    first_path, first = save(original)
    first_bytes = first_path.read_bytes()
    assert first["material"] == original["material"]
    assert first["brief"] == original["brief"]
    assert run("show", project, "0001", "--material-only") == original["material"]
    checks.append("Exact input material and brief preserved, including whitespace and Unicode")

    draft = dict(original, stage="draft", material="I have given the problem a name.")
    second_path, second = save(draft)
    assert second["_snapshot"]["parent"] == "0001"
    assert first_path.read_bytes() == first_bytes
    checks.append("New draft appends with parent and leaves original bytes unchanged")

    revision = dict(draft, stage="revision", material="I have given up more neatly.",
                    feedback=[{"kind": "simulated", "text": "Make it quieter."}])
    third_path, third = save(revision)
    assert third["feedback"] == revision["feedback"]
    checks.append("Feedback kind and exact text survive save and readback")

    recovered_path = Path(run("save", project, "--input", first_path).strip())
    recovered = json.loads(recovered_path.read_text())
    assert recovered["material"] == original["material"]
    assert recovered["_snapshot"]["copied_from"] == "0001"
    assert recovered["_snapshot"]["parent"] == "0003"
    assert first_path.read_bytes() == first_bytes
    checks.append("Recovering an old snapshot creates a new latest version")

    _, branched = save(revision, "--parent", "0002")
    assert branched["_snapshot"]["parent"] == "0002"
    assert json.loads(run("show", project, "latest"))["_snapshot"]["revision"] == "0005"
    assert len(run("list", project).splitlines()) == 5
    checks.append("Explicit branch parent, listing, and latest selection work")

    before = {p.name: p.read_bytes() for p in (project / "versions").iterdir()}
    run("save", project, "--input", "-", data={"material": "invalid"}, ok=False)
    run("save", project, "--input", "-", "--parent", "9999", data=original, ok=False)
    run("show", project, "../0001", ok=False)
    assert before == {p.name: p.read_bytes() for p in (project / "versions").iterdir()}
    checks.append("Malformed input, missing parent, and invalid revision fail without changing files")

    partial = project / "versions/0006.json"
    partial.write_text('{"unfinished":', encoding="utf-8")
    run("save", project, "--input", "-", data=original, ok=False)
    assert partial.read_text() == '{"unfinished":'
    assert len(list((project / "versions").iterdir())) == 6
    checks.append("An interrupted latest file is retained and blocks silent continuation")

    print(json.dumps({"status": "PASS", "checks": checks,
                      "retained_artifacts": str(project), "python": sys.version.split()[0]}, indent=2))


if __name__ == "__main__":
    main()
