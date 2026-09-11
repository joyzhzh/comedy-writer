# Tests and limitations

From the repository root, run:

```sh
python3 tests/test_snapshots.py
```

Python 3.9+ is sufficient; there are no third-party test dependencies. The test
creates a temporary project, keeps its files available for inspection, and prints
the resulting folder. Do not commit that machine-specific output.

The seven checks cover exact original material and brief preservation; new
versions without overwriting the original; feedback readback; recovery as a new
version; explicit branch parents and latest selection; rejection of malformed
requests without changing files; and retention of an interrupted latest file.

The writing example is an author demonstration. It is not a comparison against
a baseline, an independent review, or evidence of improved audience response.
Funniness, voice fit, global originality, and performance timing remain matters
for actual use and feedback. Chinese behavior is not validated by this package.

The skill's YAML frontmatter and UI metadata have been checked with the local
skill-creator validator and a YAML parser. The helper is tested separately from
the model's creative judgment. Automatic skill selection can depend on the host;
explicitly loading SKILL.md provides a direct invocation route.
