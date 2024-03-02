SOURCE_DIR = app

start:
	poetry run gunicorn --worker-class uvicorn.workers.UvicornWorker app.main:app

lints:
	poetry run ruff check --fix ${SOURCE_DIR}/*
	poetry run black ${SOURCE_DIR}/*

coverage:
	coverage run -m pytest && coverage report -m