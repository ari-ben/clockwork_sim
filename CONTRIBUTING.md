# Contributing

## Workflow

- `main` is protected: no direct pushes, no force pushes. Every change arrives
  through a pull request and is **squash-merged**, so `main` has one commit per
  step.
- Branch names: `<author>/<topic>`, e.g. `claude/skeleton`, `ari/timing-adrs`.
  Head branches are deleted automatically after merge.
- One pull request per step. A step is small enough to review in one sitting.

## What a pull request contains

A step changes documents and code together. A pull request:

1. updates every document its change affects: requirements, ADRs, design,
   roadmap. A status marker such as *Planned* or *Not implemented* is true only
   if the code in the same pull request makes it true;
2. adds or changes code with tests for every new path, including the guards;
3. passes `make check` locally and in CI.

Decisions that set semantics (timing, write and retention rules, advancement,
clocks) go into an ADR first, in their own pull request, before the code that
implements them.

## Checks

| Command | What it runs |
| --- | --- |
| `make format` | Ruff format and auto-fixable lint fixes |
| `make lint` | Ruff lint |
| `make typecheck` | Pyright, strict |
| `make test` / `make cov` | Pytest, without / with branch coverage |
| `make check` | All of the above, as CI runs it |

## Dependencies

- The simulation core imports the standard library only.
  `tests/test_dependencies.py` enforces this; extend its `CORE_MODULES` when a
  core module is added.
- Third-party packages go into an optional extra in `pyproject.toml`
  (`analysis`, `export`, `examples`), and the module that needs them is never
  imported from the package `__init__`.
- `uv add --optional <extra> <pkg>` or `uv add --dev <pkg>`; commit the updated
  `uv.lock`.

## Commit messages

Imperative subject of at most 72 characters, a blank line, then the why. Squash
merging uses the pull request title and description, so write those with the
same care.
