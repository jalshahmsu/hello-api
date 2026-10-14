VENV = .venv

.PHONY: install run format lint typecheck check hooks

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

install: $(VENV)/bin/activate
	$(VENV)/bin/pip install -e ".[dev]"

run:
	$(VENV)/bin/uvicorn hello_api.main:app --reload --port 8000



format:
	$(VENV)/bin/ruff format .
	$(VENV)/bin/ruff check --fix .

lint:
	$(VENV)/bin/ruff format --check .
	$(VENV)/bin/ruff check .

typecheck:
	$(VENV)/bin/mypy

check: lint typecheck

hooks:
	$(VENV)/bin/pre-commit install
