
default: test clean


test:


	python -m unittest


clean: 
	find . | grep -E "__pycache__|\.pyc$$" | xargs rm -rf