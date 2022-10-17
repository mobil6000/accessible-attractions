PYTHONPATH := $(shell poetry env info -p)


# target: help - Display callable targets
help:
	@poetry version
	@echo -e "\n\nAvailable commands:"
	@grep -E "^# target:" makefile | awk -F ": " '{print $$2}'


# target: install-dev-dependencies - creates a virtual python environment for development
install-dev-dependencies:
	@poetry check && poetry install


# target: install-prod-dependencies - creates a virtual python environment for production
install-prod-dependencies:
	@poetry check && poetry install --no-dev


# target: install-pre-commit - installs a set of pre-commit hooks for the project
install-pre-commit:
	@poetry run pre-commit install


# target: configure-prod - configures the production environment
configure-prod:
	@DJANGO_ENV=production poetry run python manage.py check --deploy --fail-level WARNING
	@sed 's~workdir~$(CURDIR)~g;s~venvpath~$(PYTHONPATH)~g' \
	./config_templates/accessible-attractions-backend.service.in > ./production/accessible-attractions-backend.service


# target: setup-dev - deploys development environment: installs the necessary dependencies, generates a file with environment variables and configures pre-commit hooks
setup-dev: install-dev-dependencies install-pre-commit .env
	@poetry run python manage.py check


# target: setup-prod - deploys the production environment: installs the necessary dependencies and configures the file with environment variables
setup-prod: install-prod-dependencies .env
	@echo "You must fix the values of the variables in the <.end> file according to your runtime!"


# target: check-env - runs checks for sintex of the file with environment variables
check-env: .env
	@poetry run dotenv-linter .env config_templates/env.template


# target: .env - generates the file with environment variables for the project
.env:
	@test ! -f .env && poetry run dump-env -t config_templates/env.template -p 'SECRET_' > .env


# target: lint - runs static checks for the source code
lint: check-env
	@poetry run flake8 && poetry run mypy


# target: test - runs all auto tests for the project
test:
	@poetry run pytest


# target: shell - runs interactive python shell with prepaired django settings for the project
shell:
	@poetry run python manage.py shell


# target: make-migrations - creates the database migrations for django models
make-migrations:
	@poetry run python manage.py makemigrations


# target: apply-migrations - apply all database migrations
apply-migrations:
	@poetry run python manage.py migrate


# target: run-dev-server - runs django web server for development on port 8000
run-dev-server:
	@poetry run python manage.py runserver

.PHONY: setup-dev setup-prod lint test make-migrations apply-migrations run-dev-server shell
