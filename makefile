install-dev-dependencies:
	@poetry check && poetry install


install-prod-dependencies:
	@poetry check && poetry install --no-dev && poetry run python manage.py check


install-pre-commit-hook:
	@poetry run pre-commit install


setup-development-env: install-dev-dependencies install-pre-commit-hook .env
setup-production-env: install-prod-dependencies .env


check-environment: .env
	@poetry run dotenv-linter .env config_templates/env.template


.env:
	@test ! -f .env && poetry run dump-env -t config_templates/env.template -p 'SECRET_' > .env
	@echo "if you are deploying a production environment, you must fix the values of the variables in the <.end> file according to your runtime!"


lint: check-environment
	@poetry run flake8 && poetry run mypy


test:
	@poetry run pytest


shell:
	@poetry run python manage.py shell


make-migrations:
	@poetry run python manage.py makemigrations


apply-migrations:
	@poetry run python manage.py migrate


run-dev-server:
	@poetry run python manage.py runserver

.PHONY: setup-development-env setup-production-env lint test make-migrations apply-migrations run-dev-server shell
