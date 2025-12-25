set shell := ["bash", "-lc"]

bootstrap:
	uv venv .venv
	uv sync

repl:
	ipython

test:
	pytest

type:
	pyright

lint:
	ruff check .

fmt:
	ruff format .

# usage: just mod co-01-python-core-for-operators
mod MODULE:
	hx "dist/modules/{{MODULE}}/THEORY.md" "dist/modules/{{MODULE}}/DRILLS.md"

rg PATTERN:
	rg -n "{{PATTERN}}" dist/modules tests src || true

health:
	python -c "import sys; print('python:', sys.executable); print('prefix:', sys.prefix)"
