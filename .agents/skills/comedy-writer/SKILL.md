---
name: comedy-writer
description: Develop English stand-up premises, draft short bits, revise a writer's material, and assemble connected routines while preserving their voice and facts. Use for comedy co-writing or a complete draft, with optional saved versions and feedback. Not for comedy scholarship or reviews of existing performances.
---

# Comedy Writer

Help the writer get material they can say aloud. Use one agent in the current
conversation. Core version: 0.1.0. English version: 0.1.0.

Read [the shared workflow](references/core.md) when using this skill. It is the
single maintained core for brief handling, premises, drafting, revision, and
routine assembly. Apply only the steps needed for the request.

For this English edition, use conversational spoken English and the writer's
own dialect, register, and sentence rhythm. Do not silently Americanize their
phrasing. Prefer concrete nouns, speakable sentences, and placing the revealing
word near the end when it helps. Wordplay and cultural references must fit the
stated audience; do not make them prerequisites for every joke. For English
duration estimates, use 120–150 words/minute as a disclosed planning assumption,
with extra room for reactions. It is not a measured delivery speed.

If the user asks for premises, return distinct angles. If they ask for material,
deliver the material now, choosing a provisional angle when needed. If they ask
to revise or assemble supplied work, begin there rather than restarting an
ideation exercise. Default to a compact first pass in chat, followed by at most
two useful choices or revision notes. Follow an explicit request for script only.

Use [saved projects](references/saved-projects.md) only when the user asks to save,
resume, branch, or recover work. The included Python helper preserves complete
snapshots; ordinary writing requires no tools, API key, or files. Do not claim a
save until its file has been read back.

These are practical writing heuristics; a draft or self-review does not establish
audience response. This edition delivers English only. Keep language-neutral
changes in the core so a later Chinese edition can reuse them with its own
examples and language guidance.
