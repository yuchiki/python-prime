check-all: test lint type-check

test:
	pytest

lint:
	isort .
	black .
	flake8

type-check:
	mypy --install-types --non-interactive atcoder_helper tests
