
default: clean

test:
	python -m unittest

	pylint .

	bandit -r .

clean:
	find . | grep -E "__pycache__" | xargs rm -rf

	black .