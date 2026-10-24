# clockwork_sim

Educational, cycle-accurate hardware simulation in pure Python: describe
microarchitecture as modules, latency-typed signals and clocks, simulate cycle by
cycle, trace, and visualize. A readable reference model and executable spec for a
later production port.

## Status

Pre-alpha. The project is being rebuilt step by step from an earlier prototype,
alternating requirements, architecture and design documents with code, tests and
examples. Nothing here is a usable API yet.

## Scope

- **Readable first.** Idiomatic Python, no C extensions, no DSL.
- **Educational.** A reference model of semantics, not a production simulator. A
  production implementation (Rust, C++ or C#) is expected to follow and to be
  checked against this one.
- **Minimal dependencies.** The simulation core uses the standard library only.
  Analysis and export are optional extras.

## Install

```bash
pip install clockwork_sim                  # core only, no third-party packages
pip install "clockwork_sim[analysis]"      # + pandas trace views
pip install "clockwork_sim[export]"        # + VCD export
pip install "clockwork_sim[all]"           # everything, including example CLIs
```

(Not published yet; install from a clone for now.)

## Development

Requires [uv](https://docs.astral.sh/uv/). It installs the pinned Python version
itself.

```bash
git clone https://github.com/ari-ben/clockwork_sim
cd clockwork_sim
make sync     # create .venv with all extras and dev tools, from uv.lock
make check    # format check, lint, strict type check, tests with coverage
make help     # all targets
```

CI runs `make check` on Python 3.12 and 3.13. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the workflow.

## License

MIT. See [LICENSE](LICENSE).
