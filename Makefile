install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=validator

lint:
	poetry run flake8 validator tests

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build