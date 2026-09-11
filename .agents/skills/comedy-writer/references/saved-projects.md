# Optional saved projects

Use a user-selected folder. If the user asks to save without naming a destination,
choose a new descriptive folder under the current workspace's `writing-projects/`
and tell them where it is. Do not save into the installed skill's source files.
If filesystem access is unavailable, provide the complete snapshot in chat and
state that it was not saved. Keep ordinary chat writing free of this bookkeeping.

Use `scripts/snapshots.py` relative to the skill folder, with Python 3.9+ and no
third-party packages. It only creates new numbered JSON files. There is no delete
or overwrite command. Each snapshot contains enough context to resume by itself.

Prepare this JSON in a new input file, or send it on standard input with `--input -`:

```json
{
  "title": "Calendar bit",
  "stage": "draft",
  "brief": {
    "language": "en",
    "request": "A short bit about calendar reminders",
    "facts": ["I put a reminder in my calendar to relax."],
    "voice": "Quiet, literal, self-deprecating",
    "boundaries": ["No invented personal incidents"],
    "selected_premise": "Relaxing has become another deadline"
  },
  "material": "I put a reminder in my calendar to relax. Now I'm behind on that too.",
  "feedback": [],
  "revision_notes": ["First draft; metaphorical extension of the supplied fact."]
}
```

Valid stages: `input`, `premises`, `draft`, `revision`, `routine`. Add useful brief
fields such as audience, duration, exact voice sample, or approved inventions.
When useful, preserve editable `brief.source_notes` from
[topical writing](topical-material.md) and `brief.routine_plan` from
[beat planning](routine-planning.md). These are optional JSON conventions: the
helper retains them without verifying facts, links, permissions, or dependencies.
They do not introduce a transcript importer or a new snapshot schema. Old 0.1.0
snapshots remain readable; recovering one appends a 0.2.0 snapshot and leaves the
old file and its version metadata intact.
Keep unknown facts unknown. Preserve the user's original material verbatim in an
`input` snapshot before saving a rewrite. Separate feedback kinds in the list:
`writer`, `audience-reported`, `self-review`, or `simulated`. Only use `writer` for
the actual writer's words; examples with invented feedback use `simulated`.

Commands (replace the example paths with actual absolute paths):

```sh
python3 /path/to/skill/scripts/snapshots.py save /path/to/project --input /path/to/new-input.json
python3 /path/to/skill/scripts/snapshots.py list /path/to/project
python3 /path/to/skill/scripts/snapshots.py show /path/to/project latest
python3 /path/to/skill/scripts/snapshots.py show /path/to/project 0001 --material-only
```

After saving, read back the returned revision and verify its material and brief.
Return a clickable link to that JSON file. The user normally just asks to save;
the agent handles these commands.

To resume, read `latest` and its feedback before editing. Each file is a full
snapshot, not a delta. To recover an earlier draft, show its material. To make
it the latest again, save that old JSON with `--input`; this creates another
revision and records `copied_from`. To develop a deliberate branch, add
`--parent 0001` while saving a new input. Existing versions remain intact.
`latest` selects the highest numbered file and validates it before use. A partial
or invalid latest file raises an error rather than silently choosing an older one.
Check the saved parent when continuing branches.

Do not edit old snapshots, user input files, or competing candidates in place.
Keep rejected alternatives in prior versions or the current notes. Do not stage,
commit, or transmit personal drafts unless requested. Local version history is
not a remote backup. If a write is interrupted, retain the partial file and report
the error; inspect earlier valid snapshots rather than overwriting it.
