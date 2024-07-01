.PHONY: install
install:
	poetry install

.PHONY: flake8
flake8:
	poetry run flake8

.PHONY: migrate
migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: runserver
runserver:
	. venv/scripts/activate && poetry run python manage.py runserver

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser

pre-commit:
	poetry run pre-commit run --all-files

.PHONY: udpate
update: install migrate;

.PHONY: shell
shell:
	poetry run python manage.py shell

.PHONY: celery-worker
celery-worker:
	poetry run celery -A project worker -l info
