# fit-configurations

Configuration module for the **FIT Project**, built using [PySide6](https://doc.qt.io/qtforpython/).

This module provides the graphical interface for configuring settings used by the FIT application.

---

## 🐍 Dependencies

Main dependencies are:

- **Python** >=3.11,<3.14
- **Poetry** (recommended for development)
- [`PySide6`](https://pypi.org/project/PySide6/) 6.9.0
- [`SQLAlchemy`](https://pypi.org/project/SQLAlchemy/) ^2.0.40
- [`fit-common`](https://github.com/fit-project/fit-common)  – shared utility and core logic
- [`fit-assets`](https://github.com/fit-project/fit-assets)  – UI resources and assets

See `pyproject.toml` for full details.

---

## Local checks (same as CI)

Run these commands before opening a PR, so failures are caught locally first.

### What each tool does
- `pytest`: runs automated tests (`unit`, `contract`, and `integration` suites).
- `ruff`: checks code style and common static issues (lint).
- `mypy`: performs static type checking on annotated Python code.
- `bandit`: scans source code for common security anti-patterns.
- `pip-audit`: checks installed dependencies for known CVEs.

### 1) Base setup
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install . pytest ruff mypy "bandit[toml]" pip-audit
```

### 2) Test suite
```bash
export QT_QPA_PLATFORM=offscreen

# unit tests
pytest -m unit -q tests

# contract tests
pytest -m contract -q tests

# integration tests (requires fit-assets package)
pytest -m integration -q tests

# end-to-end smoke tests
pytest -m e2e -q tests
```

### 3) Quality and security checks
```bash
ruff check fit_configurations tests
mypy fit_configurations
bandit -c pyproject.toml -r fit_configurations -q -ll -ii
pip-audit --progress-spinner off
```

Note: `pip-audit` may print a skip message for `fit-common` and `fit-assets`  because it is a local package and not published on PyPI.

---

## Installation

``` bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install poetry
    poetry lock
    poetry install
    poetry run python main.py
```
