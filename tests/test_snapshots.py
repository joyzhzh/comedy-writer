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

    # Exercise the new optional context through the same public CLI used by saves.
    extended_project = project / "optional-context"
    extended_brief = dict(original["brief"], source_notes=[{
        "id": "n1", "claim": "A bench booking policy was mentioned without a source.",
        "basis": "unverified", "limits": ["No policy document inspected"],
        "comic_angle": "A hypothetical appointment to sit down",
    }], routine_plan={
        "through_line": "Making rest into work", "beats": [
            {"id": "b1", "purpose": "Introduce hypothetical booking", "needs": []},
            {"id": "b2", "purpose": "Return to booking", "needs": ["b1"]},
        ], "order": ["b1", "b2"], "open_questions": ["Keep the return?"],
    })
    extended = dict(original, brief=extended_brief)
    extended_path = Path(run("save", extended_project, "--input", "-", data=extended).strip())
    extended_bytes = extended_path.read_bytes()
    shown = json.loads(run("show", extended_project))
    assert shown["brief"] == extended_brief
    branch_path = Path(run("save", extended_project, "--input", extended_path,
                           "--parent", "0001").strip())
    assert json.loads(branch_path.read_text())["brief"] == extended_brief
    assert extended_path.read_bytes() == extended_bytes
    checks.append("Optional source notes and routine context survive show and branch unchanged")

    # A real schema-1 layout from the previous version, not written by the new helper.
    legacy_project = project / "legacy"
    legacy_folder = legacy_project / "versions"
    legacy_folder.mkdir(parents=True)
    legacy = dict(original, _snapshot={
        "schema": 1, "revision": "0001", "parent": None, "copied_from": None,
        "created_utc": "2026-09-01T00:00:00+00:00",
        "core_version": "0.1.0", "english_version": "0.1.0",
    })
    legacy_path = legacy_folder / "0001.json"
    legacy_path.write_text(json.dumps(legacy, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    legacy_bytes = legacy_path.read_bytes()
    assert json.loads(run("show", legacy_project)) == legacy
    restored_path = Path(run("save", legacy_project, "--input", legacy_path).strip())
    restored = json.loads(restored_path.read_text())
    assert restored["material"] == legacy["material"]
    assert restored["brief"] == legacy["brief"]
    assert restored["_snapshot"]["schema"] == 1
    assert restored["_snapshot"]["copied_from"] == "0001"
    assert restored["_snapshot"]["parent"] == "0001"
    assert restored["_snapshot"]["core_version"] == "0.2.0"
    assert restored["_snapshot"]["english_version"] == "0.2.0"
    assert legacy_path.read_bytes() == legacy_bytes
    checks.append("A 0.1.0 snapshot reads exactly and recovers as 0.2.0 without changing the old file")

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
