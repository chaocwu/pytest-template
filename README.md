# pytest-template

**_description_**

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit/main.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pre-commit/main)

## uv

An extremely fast Python package and project manager, written in Rust.

For more information see: https://docs.astral.sh/uv

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
uv self update
cd pytest-template
uv sync
uv tool install ruff
uv tool upgrade --all
uv tool run ruff check
uvx ruff check
```

## pre-commit

A framework for managing and maintaining multi-language pre-commit hooks.

For more information see: https://pre-commit.com/

```bash
pre-commit install
pre-commit autoupdate
pre-commit run --all-files
```

## pytest

The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

For more information see: https://docs.pytest.org/en/stable/

```bash
pytest testing/
pytest test_mod.py
pytest tests/test_mod.py::test_func
pytest tests/test_mod.py::TestClass
pytest tests/test_mod.py::TestClass::test_method
pytest -k 'MyClass and not method'
pytest -m slow
```