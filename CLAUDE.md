# Notes for Claude sessions

Read CONTRIBUTING.md; it is the source of truth for workflow. In short:

- Work on a `claude/<topic>` branch and open a pull request against `main`;
  never push to `main`. Squash merge only (the maintainer merges).
- One step per pull request. Documents and code change together; an ADR
  precedes any change to simulation semantics.
- Run `make check` before pushing. It must pass on Python 3.12 and 3.13.
- The core (`src/clockwork_sim`, excluding analysis/export submodules) is
  stdlib-only. Never import pandas, numpy, pyvcd, typer or rich from it or from
  the package `__init__`.
- Prefer readability over cleverness: this is an educational reference model
  that a later Rust/C++/C# port will be checked against. Avoid Python-only
  tricks (dynamic `__getattr__` APIs, identity-based behaviour) that a port
  could not reproduce.
- The earlier prototype is reference material only. Port from it deliberately,
  module by module, and fix its known issues as you go (they will be recorded
  in the roadmap once the docs are imported).
