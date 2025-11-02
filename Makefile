install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml --cov-report term-missing

lint:
	uv run flake8 gendiff

check: lint test

.PHONY: install test test-coverage lint check
