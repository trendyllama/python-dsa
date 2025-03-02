

.PHONY: clean build

clean:
	rm -rf .venv/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf */__pycache__
	rm -rf */*egg-info

build:
	uv sync

test:
	pytest
