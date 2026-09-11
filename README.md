# Comedy Writer

A small English stand-up co-writing skill for Codex. Develop premises, draft short
bits, revise existing material, or connect several bits into a routine. Work in
conversation or ask for a complete first draft.

Version 0.2.0 is an early prototype. It preserves supplied facts and voice as
writing constraints, supports feedback, and can save recoverable draft versions.
It adds a 16-technique writing menu, source notes for topical material, optional
routine beat maps, and source-linked performer study guidance. These references
load when relevant; ordinary drafting stays a conversation.
Its writing heuristics and model judgments do not guarantee a funny result.

## Use it

Clone this repository and open the checkout as your Codex project:

```sh
git clone https://github.com/joyzhzh/comedy-writer.git
cd comedy-writer
```

The skill lives in `.agents/skills/comedy-writer/`. Invoke it with `$comedy-writer`.
You can also explicitly ask Codex to read the `SKILL.md` at that location in your
checkout. See [Codex's skill documentation](https://learn.chatgpt.com/docs/build-skills)
for local discovery details.

Try any of these prompts:

- **Premises:** “$comedy-writer Give me three different angles on how my calendar
  turns relaxing into a deadline. Quiet and self-deprecating.”
- **Draft:** “$comedy-writer Write a 45-second bit. I bought a label maker to get
  organized, then labelled the drawer full of cables 'miscellaneous'. Keep it dry
  and don't invent additional personal incidents.”
- **Revise:** “$comedy-writer Light punch-up of this draft. Keep my opening and
  facts, cut explanation, and give me two possible endings: [paste draft].”
- **Assemble:** “$comedy-writer Connect these bits into about two minutes, with
  transitions and a closing payoff: [paste bits].”
- **Learn:** “$comedy-writer Explain callbacks, misdirection, and escalation with
  original examples and one short exercise.”
- **Topical:** “$comedy-writer Help me find a comic angle on this announcement.
  Check its factual anchor and keep source notes separate: [source link].”

You can specify audience, tone, boundaries, length, and whether you want choices
or a script. For no explanation, request “script only.” You can then give feedback
such as “too polished,” “quieter,” or “keep the first paragraph.”

## Save and resume

Ask the agent to save a writing project, optionally naming a destination. It
preserves original material and creates new numbered JSON snapshots containing
the brief, draft, feedback, and revision notes. Ask to resume, show an earlier
version, branch from it, or recover it as a new version.

Ordinary writing needs no scripts or API setup. Topical source checking uses the
host's browsing capability when available. Optional local saves use Python
3.9+ and the standard library. The helper makes no network requests. It does not
change how the host Codex application handles conversation data.

The default `writing-projects/` folder is Git-ignored. If you choose another folder
inside this checkout, ignore it before committing. Saved personal drafts should
not become repository contributions. Local snapshots are not a cloud backup.

## Learn more

- [Writing and revision example](docs/EXAMPLE.md)
- [Where the writing guidance comes from](docs/WRITING_GUIDANCE.md)
- [Complete edition references](.agents/skills/comedy-writer/references/sources.md)
- [Technique catalogue](.agents/skills/comedy-writer/references/techniques.md)
- [Performer study and script access](.agents/skills/comedy-writer/references/study-guide.md)
- [Concrete reuse decisions](docs/REUSE_DECISIONS.md)
- [0.2.0 behavior demonstrations](docs/UPGRADE_EXAMPLES.md)
- [Tests and current limitations](docs/TESTING.md)
- [Optional snapshot commands](.agents/skills/comedy-writer/references/saved-projects.md)

The shared workflow is maintained once in `references/core.md`, with English
guidance in `SKILL.md`. This package currently delivers English only.

No open-source license has been selected for this repository yet.
