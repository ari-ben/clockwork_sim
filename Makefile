# Single entry point for local work and every CI system (GitHub Actions today,
# GitLab CI later). CI calls `make check` and nothing else, so the two can
# never drift apart.

UV ?= uv
SRC := src tests

.PHONY: help sync lint format format-check typecheck test cov check clean

help:  ## List targets
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-13s %s\n", $$1, $$2}'

sync:  ## Create/update .venv from uv.lock (all extras + dev tools)
	$(UV) sync --all-extras --locked

lint:  ## Ruff lint
	$(UV) run ruff check $(SRC)

format:  ## Ruff format (rewrites files)
	$(UV) run ruff format $(SRC)
	$(UV) run ruff check --fix $(SRC)

format-check:  ## Ruff format, check only
	$(UV) run ruff format --check $(SRC)

typecheck:  ## Pyright, strict
	$(UV) run pyright

test:  ## Pytest
	$(UV) run pytest

cov:  ## Pytest with branch coverage report
	$(UV) run pytest --cov --cov-report=term-missing

check: sync format-check lint typecheck cov  ## Everything CI runs

clean:  ## Remove caches and build outputs
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov dist build
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
