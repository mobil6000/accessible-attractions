install-dev-dependencies:
	@poetry check && poetry install


setup-development-env: install-dev-dependencies .env


check-environment: .env
	@poetry run dotenv-linter .env config/.env.template


.env:
	@test ! -f .env && poetry run dump-env -t config/.env.template -p 'SECRET_' > .env
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
