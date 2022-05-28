install-dev-dependencies:
	@poetry check && poetry install


install-pre-commit-hook:
	@poetry run pre-commit install


setup-development-env: install-dev-dependencies install-pre-commit-hook .env


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


run-dev-server:
	poetry run python manage.py runserver

.PHONY: setup-development-env lint test run-dev-server shell
