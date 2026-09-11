# Reuse decisions in 0.2.0

This edition implements two small workflow ideas in its own guidance. It does
not vendor or execute external comedy-writing code, replace its model, or add a
dependency. The writing and snapshot workflow stays in the current conversation.

| Candidate idea | Decision implemented | Why this scope |
|---|---|---|
| [Jokeasy's editable source-linked inspiration](https://yate.fun/projects/jokeasy/) | Optional editable source notes separate a factual anchor from a comic angle. | Useful for topical material; ordinary personal bits need no news-retrieval pipeline. A reusable public code repository was not established. |
| [Dramatron's use of prior structured context](https://github.com/google-deepmind/dramatron) | An optional small beat map records context and callback dependencies for routines. | Useful for ordering problems; a full theatre-writing hierarchy is unnecessary for a short bit. No framework code was adopted. |
| Multi-agent generation, model adapters, recognition datasets, and automated transcript services | Deferred from this edition. | No demonstrated need or measured writing benefit established for this small workflow; integration, source provenance, and data permissions would need their own work. |

The concrete additions are [source notes](../.agents/skills/comedy-writer/references/topical-material.md)
and [routine planning](../.agents/skills/comedy-writer/references/routine-planning.md).
Both can be retained as optional brief data in existing snapshots. The helper
does not validate their factual or creative content. These are idea adaptations,
not claims that earlier versions were built on those repositories.

See the [bibliography](../.agents/skills/comedy-writer/references/sources.md) for
attribution, inspected material, and limits. The adaptations have author
demonstrations and storage checks; their effect on writing quality is unmeasured.
