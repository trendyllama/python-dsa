
default: all

setup:

	black .

	isort .

test:
	python -m unittest

	pylint .

build:

	poetry build


clean:
	find . | grep -E "__pycache__" | xargs rm -rf

	rm -rf dist/


all: setup test build