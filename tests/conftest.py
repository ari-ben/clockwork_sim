"""Shared test configuration.

Per testing.md § 2.2, this file holds two kinds of shared code only:

- minimal ``Module`` subclasses (Producer, Forwarder, Consumer) used by more
  than one test module, so library types can be narrowed to ``Module``
  instead of being held open for mocks;
- autouse fixtures that reset global state around every test.

Both are added together with the code they serve: the module fixtures with
``Module``, the reset fixture with the recorder. Setup that *is* the scenario
stays inline in the test.
"""
