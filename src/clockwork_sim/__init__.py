"""Clockwork: educational, cycle-accurate hardware simulation in pure Python.

The simulation core (context, clock, signal, module, orchestrator, recorder)
depends on the standard library only. Analysis and export layers live in
submodules that are imported explicitly and need the optional extras
``clockwork_sim[analysis]`` / ``clockwork_sim[export]``. Nothing in this
package's ``__init__`` may import them.
"""

__version__ = "0.0.1"

__all__ = ["__version__"]
