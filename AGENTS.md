# AI Agent Instructions for python-dsa

- Check for any code duplication and suggest abstracting it out

## Purpose
This repository is a Python learning project for data structures, algorithms, and related examples. Most code lives under `src/`, with tests under `tests/`.


## Recommended commands
Use the repository's `uv` tasks and `pyproject.toml` settings.
- `uv run format` — format code with `ruff`.
- `uv run lint` — run lint checks with `ruff`.
- `uv run test` — run tests with `pytest`.

- Do not use ripgrep (`rg`)

For manual commands:
- `python -m pytest`
- `python -m ruff check`
- `python -m ruff format`

## What to inspect first
- `pyproject.toml` for dependency, formatter, and lint configuration.
- `README.md` for the project description.
- `src/` for algorithm, data structure, and Codecademy example modules.
- `tests/` for expected behavior and usage patterns.


## Useful references
- Repository README: `README.md`
- Python project settings: `pyproject.toml`
- Build/test commands: use `uv` task definitions in the workspace.
