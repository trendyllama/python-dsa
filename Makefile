
default: clean

test:
	python -m unittest

	pylint .

clean:
	find . | grep -E "__pycache__" | xargs rm -rf

	black .