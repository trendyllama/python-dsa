---
description: these instructions should be applied when working with python tests in this repository.
applyTo: '**/tests/**/*.py'

---

- Use `pytest` as the testing framework for all Python tests in this repository.

- Add tests to `tests/` directory that correspond to the modules in `src/` directory.

- Make sure outputs are adaptable and not hardcoded - for example my `recipies.json` file can be modifed, recipies can be added or removed, so the tests should not assume a fixed number of recipes or specific recipe names.

