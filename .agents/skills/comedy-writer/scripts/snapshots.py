#!/usr/bin/env python3
"""Append local comedy drafts as self-contained JSON snapshots; never overwrite."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys

STAGES = {"input", "premises", "draft", "revision", "routine"}
FEEDBACK_KINDS = {"writer", "audience-reported", "self-review", "simulated"}


def validate(data):
    if not isinstance(data, dict):
        raise ValueError("Snapshot must be a JSON object.")
    for key in ("title", "material"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"{key} must be a nonempty string.")
    if data.get("stage") not in STAGES:
        raise ValueError("stage must be input, premises, draft, revision, or routine.")
    brief = data.get("brief")
    if not isinstance(brief, dict):
        raise ValueError("brief must be an object containing facts and voice.")
    if not isinstance(brief.get("facts"), list) or not all(
        isinstance(item, str) for item in brief["facts"]
    ):
        raise ValueError("brief.facts must be a list of strings (empty is allowed).")
    if not isinstance(brief.get("voice"), str):
        raise ValueError("brief.voice must be a string.")
    feedback = data.get("feedback", [])
    if not isinstance(feedback, list) or not all(
        isinstance(item, dict) and item.get("kind") in FEEDBACK_KINDS
        and isinstance(item.get("text"), str) for item in feedback
    ):
        raise ValueError("feedback must contain objects with a known kind and text.")
    notes = data.get("revision_notes", [])
    if not isinstance(notes, list) or not all(isinstance(item, str) for item in notes):
        raise ValueError("revision_notes must be a list of strings.")
    return data


def versions(project):
    return sorted(
        (p for p in (project / "versions").glob("*.json")
         if re.fullmatch(r"[0-9]{4,}\.json", p.name)),
        key=lambda p: int(p.stem),
    )


def select(project, revision):
    if revision == "latest":
        found = versions(project)
        if not found:
            raise ValueError("No snapshots saved yet.")
        return found[-1]
    if not re.fullmatch(r"[0-9]{4,}", revision):
        raise ValueError("Use a revision such as 0001, or latest.")
    path = project / "versions" / f"{revision}.json"
    if not path.is_file():
        raise ValueError(f"Revision {revision} does not exist.")
    return path


def read(path):
    data = validate(json.loads(path.read_text(encoding="utf-8")))
    meta = data.get("_snapshot")
    if not isinstance(meta, dict) or meta.get("revision") != path.stem:
        raise ValueError(f"Invalid snapshot metadata in {path}; file retained.")
    return data


def save(project, input_name, parent):
    raw = sys.stdin.read() if input_name == "-" else Path(input_name).read_text(encoding="utf-8")
    data = validate(json.loads(raw))
    previous = versions(project)
    parent_path = select(project, parent) if parent else (previous[-1] if previous else None)
    if parent_path:
        read(parent_path)  # Refuse to silently continue an interrupted/invalid latest save.
    old_meta = data.pop("_snapshot", {})
    if not isinstance(old_meta, dict):
        raise ValueError("_snapshot metadata must be an object when provided.")
    number = int(previous[-1].stem) + 1 if previous else 1
    folder = project / "versions"
    folder.mkdir(parents=True, exist_ok=True)
    while True:
        revision = f"{number:04d}"
        path = folder / f"{revision}.json"
        data["_snapshot"] = {
            "schema": 1,
            "revision": revision,
            "parent": parent_path.stem if parent_path else None,
            "copied_from": old_meta.get("revision"),
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "core_version": "0.1.0",
            "english_version": "0.1.0",
        }
        payload = json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        try:
            stream = path.open("x", encoding="utf-8")
        except FileExistsError:
            number += 1
            continue
        with stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        if read(path) != data:
            raise ValueError(f"Readback mismatch at {path}; file retained.")
        return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    saving = commands.add_parser("save", help="Create a new snapshot from JSON.")
    saving.add_argument("project", type=Path)
    saving.add_argument("--input", required=True, help="JSON path, or - for stdin")
    saving.add_argument("--parent", help="Existing revision to branch from")
    listing = commands.add_parser("list", help="List saved revisions.")
    listing.add_argument("project", type=Path)
    showing = commands.add_parser("show", help="Read a snapshot or its material.")
    showing.add_argument("project", type=Path)
    showing.add_argument("revision", nargs="?", default="latest")
    showing.add_argument("--material-only", action="store_true")
    args = parser.parse_args()
    project = args.project.expanduser().resolve()
    try:
        if args.command == "save":
            print(save(project, args.input, args.parent))
        elif args.command == "show":
            data = read(select(project, args.revision))
            if args.material_only:
                sys.stdout.write(data["material"])
            else:
                print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            for path in versions(project):
                data = read(path)
                print(f"{path.stem}\t{data['stage']}\t{data['title']}")
    except (OSError, ValueError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
