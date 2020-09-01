clean:
	rm -rf __pycache__ */__pycache__ */**/__pycache__

clean-migrations: clean
	find */migrations -type f -not -name '__init__.py' -delete

migrate:
	python manage.py migrate

run:
	python manage.py runserver
