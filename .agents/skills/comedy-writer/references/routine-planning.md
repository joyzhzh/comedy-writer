# Optional routine beat planning

Use a small map when several bits share facts, transitions, or callbacks and the
order is causing trouble. A short bit usually needs no map. Start with the
writer's existing material and give them the connected script they requested.

For each necessary beat, note its purpose, what the listener must already know,
and the transition to the next beat. A callback must have an earlier seed still
present in the proposed order. Mark that dependency; do not assume a removed or
unseen seed exists. A return may serve recognition, continuity, or a new meaning.
When reordering, check for missing context, contradictory facts, and duplicated
exposition. Repair only the affected joins. Do not invent a personal event to
make the order work.

A map may be a few lines in chat. If saving is requested, this optional
`brief.routine_plan` convention can keep the planning context:

```json
{
  "through_line": "Treating household chores as a company",
  "beats": [
    {"id": "b1", "purpose": "Establish vacuum as head of housekeeping", "needs": []},
    {"id": "b2", "purpose": "Develop a separate chores beat", "needs": []},
    {"id": "b3", "purpose": "Return to housekeeping for the closer", "needs": ["b1"]}
  ],
  "order": ["b1", "b2", "b3"],
  "open_questions": []
}
```

The helper stores this data without checking graph validity or joke quality; the
agent checks the actual script. Do not add a graph framework, multiple agents, or
a mandatory outline-first process. This is an idea-level adaptation of
[Dramatron's use of prior context](sources.md#workflow-design-references), scaled
down for stand-up. It is not an implementation or evaluation of Dramatron.
