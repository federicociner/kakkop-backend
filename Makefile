clean:
	rm -rf __pycache__ */__pycache__ */**/__pycache__

clean-migrations: clean
	find */migrations -type f -not -name '__init__.py' -delete

lint:
	black -l 79 . --check

fix-lint:
	black -l 79 . && isort . -m 3 -tc

migrate:
	python manage.py migrate

run:
	python manage.py runserver
