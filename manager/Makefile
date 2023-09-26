default:

PHONY: clean check check-flake8 check-format check-typing dev-requirements format python test upgrade-postgres virtualenv

.sentinels:
	mkdir .sentinels

clean:
	pyenv virtualenv-delete micro-file-manager
	rm -rf .sentinels

.sentinels/install-python: | .sentinels
	pyenv install --skip-existing 3.11
	touch $@

python: .sentinels/install-python

.sentinels/setup-env: requirements/production.txt | .sentinels python
	pyenv virtualenv 3.11 micro-file-manager || true
	pip install -r requirements/production.txt
	touch $@

virtualenv: .sentinels/setup-env

.sentinels/setup-dev-env: requirements/development.txt | .sentinels
	pip install -r requirements/development.txt
	touch $@

dev-requirements: .sentinels/setup-dev-env | virtualenv

check-flake8:
	flake8 --extend-exclude='migrations,tests' --docstring-convention google .
	# don't require docstrings on tests
	flake8 --extend-ignore=D100,D101,D102,D104,D107 tests

check-format: | dev-requirements check-flake8 # TODO use sentinels to avoid re-checking unchanged files
	black --extend-exclude='migrations' --check .

check-typing: | dev-requirements # TODO use sentinels to avoid re-checking unchanged files
	mypy .

format: | dev-requirements # TODO use sentinels to avoid re-formatting unchanged files
	black .

check: check-format check-typing

postgres-upgrade: | dev-requirements
	alembic upgrade head

test: | dev-requirements
	coverage run -m unittest discover --verbose -t . -s ./tests/unit -p '*.py'
	coverage report --show-missing --fail-under=100
