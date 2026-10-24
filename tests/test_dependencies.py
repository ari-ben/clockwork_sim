"""The simulation core must import with the standard library only.

Guards requirements-core § 4.1: third-party packages are allowed solely in the
analysis and export layers, which are imported explicitly. The previous
codebase broke this by importing the trace layer (pandas, numpy) from the
package ``__init__``.

Each check runs in a fresh interpreter, so modules already imported by pytest
or by other tests cannot mask a violation.
"""

import subprocess
import sys

import pytest

import clockwork_sim

# Third-party packages that only the optional layers may use.
FORBIDDEN_IN_CORE = ("pandas", "numpy", "vcd", "typer", "rich")

# Core modules that must stay stdlib-only. Grows as the core is built.
CORE_MODULES = ("clockwork_sim",)

_BLOCKER = """
import importlib.abc
import sys

FORBIDDEN = set({forbidden!r})


class _Blocker(importlib.abc.MetaPathFinder):
    def find_spec(self, name, path=None, target=None):
        if name.split(".")[0] in FORBIDDEN:
            raise ImportError(f"core imported forbidden package {{name!r}}")
        return None


sys.meta_path.insert(0, _Blocker())
import {module}
"""


@pytest.mark.parametrize("module", CORE_MODULES)
def test_core_module_imports_without_third_party_packages(module: str) -> None:
    code = _BLOCKER.format(forbidden=FORBIDDEN_IN_CORE, module=module)
    result = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, result.stderr


def test_package_declares_no_runtime_dependencies() -> None:
    from importlib.metadata import requires

    runtime = [r for r in (requires("clockwork_sim") or []) if "extra ==" not in r]
    assert runtime == []


def test_version_matches_package_metadata() -> None:
    from importlib.metadata import version

    assert clockwork_sim.__version__ == version("clockwork_sim")
