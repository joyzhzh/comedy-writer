# Optional source notes for topical writing

Use this when a bit depends on news, an external claim, a quotation, or a source
the writer wants to study. Ordinary personal observations need no research form.
Follow the host's browsing rules. When a current claim needs verification and
browsing is available, open an appropriate primary source and inspect the relevant
body. A search snippet or a remembered headline alone is not verification.

Keep the factual anchor separate from the comic interpretation. Preserve dates,
scope, and uncertainty that affect the joke. If a claim cannot be checked, label
it as unverified, ask for the necessary source when it blocks the bit, or offer a
clearly hypothetical version. Do not convert a hypothetical into a reported event.
Keep source notes outside the performance script unless the writer asks otherwise.

An editable note can be one sentence in chat. When saving is requested,
`brief.source_notes` can hold objects with these suggested fields:

| Field | Use |
|---|---|
| `id` | A short identifier local to this writing project. |
| `claim` | A concise factual anchor in the writer's or agent's own words. |
| `basis` | `user_report`, `source_checked`, `unverified`, or `fictional`. These describe provenance, not a truth score. |
| `source_url` / `locator` | The exact source and relevant section, page, or time when available; omit unknown values. |
| `checked_at` | Actual check date when a source was inspected; do not stamp an unperformed check. |
| `limits` | Missing context, competing accounts, access barriers, or unresolved facts. |
| `comic_angle` | An editable proposed interpretation, separate from the factual claim. |

If the writer changes the source claim, reconsider its `basis` and the lines that
depend on it. A previous check does not verify newly edited wording. For a copied
quotation, verify its exact wording and attribution; otherwise paraphrase the
claim without quotation marks. Preserve fictional invention as fiction.

This adapts the editable, source-linked inspiration idea in
[Jokeasy](sources.md#workflow-design-references) and takes limited process context
from the [Daily Show writers' interview](sources.md#study-and-process-sources).
It does not implement either system, automatically ingest news, or establish a
Daily Show writing formula. The snapshot helper only retains JSON; it does not
verify a source note or authorize reuse of source text.
