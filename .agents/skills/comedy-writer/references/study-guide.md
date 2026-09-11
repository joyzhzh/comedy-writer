# Optional study of performers and topical television

Use the [five-performer, ten-work catalogue](sources.md#performer-and-work-catalogue)
to choose material to study. It is a starter ledger of sources, not a script
collection, an objective best-comedian list, or a completed analysis of ten shows.
For immediately locatable written passages, the
[study and process sources](sources.md#study-and-process-sources) offer bounded
interviews, a textual edition, and creator discussion. Keep each source's limits.

When the user wants a study note, inspect the actual permitted passage or their
supplied excerpt. Record the work, source type, exact locator, and what was
actually inspected. Distinguish a production script, edited transcript, subtitle,
automatic speech recognition, interview, and original analyst summary. Mark audio
or visuals uninspected when applicable. A catalogue listing is a lead, not evidence
of a technique in the work.

Describe the setup information, expectation, turn, subsequent beat, or transition
in your own words. Separate visible textual structure from an inference about
intent or an unobserved audience response. Keep quotations brief and source-linked;
do not reproduce full copyrighted scripts. Then make an original exercise on a
different situation. Do not retrieve a performer's punchline and lightly reword it
for the writer. A study of structure is not a request to imitate their identity.

If a saved study ledger is requested, use a separate local JSONL file with one
note per line: `id`, `work`, `source_url`, `source_type`, `locator`,
`inspected`, `observation`, `interpretation`, `technique_candidates`,
`exercise`, and `limits`. This is an optional note convention, not a supplied
importer. Keep unknowns explicit and revisions as new notes. Personal drafts and
full source captures do not belong in a public contribution.

## The Daily Show

Topical desk pieces, field segments, interviews, and audio compilations have
different context from stand-up. Identify the unit, edition, date, presenter, and
source locator. A host, correspondent, or guest is not automatically the credited
writer. Leave an unknown writer credit unknown. Missing graphics and edited or
machine-generated transcripts limit analysis of wording and delivery.

The [WGA interview](sources.md#study-and-process-sources) supplies writers'
accounts of pitching, tone, and presenter fit. Treat them as process descriptions.
For a topical writing request, use [source notes](topical-material.md) to separate
the news anchor from the comic angle. Do not present satire, an interviewee's
claim, or a machine transcript as independent verification of an external fact.

## Getting text

Start with official links, permitted excerpts, or user-supplied material.
[YouTube's official caption-download method](https://developers.google.com/youtube/v3/docs/captions/download)
requires authorization and video-editing permission;
[listing caption tracks](https://developers.google.com/youtube/v3/docs/captions/list)
does not return their text. A visible caption option or public video is insufficient
to establish an API download route for that work. Netflix's documented subtitle
controls are player features. No general production-script API was established
for Netflix or The Daily Show in this edition's documentation review.

No transcript service, scraper, automated speech recognizer, or bulk importer is
installed by this skill. If a future workflow transforms source text, retain the
original source type and explicitly label each transformation; generated text
must not silently become an “official script.” See the
[access references](sources.md#caption-and-transcript-documentation) for the exact
documentation and the limits of these checks.
