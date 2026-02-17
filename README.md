# Overview

In this repo, I build a basic python package using pip and follow software development best practices. 

* Code Styling
* Linting
* Testing
* Documenting
* Building
* Versioning
* CI/CD

# Helpful Terminal Commands

* Conda Environment: conda create -n pip_package python=3.13.5
* Activate Conda conda activate pip_package
* Install build: pip install build
* Build: python -m build
* Install: pip install .
* Install Dev: pip install -e .[dev]
* Uninstall: pip uninstall gregs_pip_package -y
* Style: ruff format .
* Lint: ruff check . --fix
* Pre-commit check: pre-commit run --all-files
* Test: pytest -v
* Document: mkdocs build --strict
* Serve documentation: mkdocs serve

# Github Actions

* Build documents on PR and merge into main.
* Ensure code follows lint rules & well formated on PR and merge into main.
* Confirm package could be published to pypi on PR and merge into main.
* Run tests on linux, mac, and windows on push and PR.


