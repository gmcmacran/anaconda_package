# Overview

In this repo, I build a basic python package using anaconda and follow software development best practices. 

* Code Styling
* Linting
* Testing
* Documenting
* Building
* Versioning
* CI/CD

This repo supports building with anaconda and pip. The typical process is to publish on pypi and then point conda at the pypi page. This package will not be published on pypi so this workflow does not work. 

Instead, this repo supports two independent build processes. Pip & conda. This causes challenges around keeping the toml file in sync with conda's meta.yml. Github actions are used to confirm both build processes work.

# Helpful Terminal Commands

### Environment setup
* Conda Environment: conda create -n anaconda_package python=3.13.5 conda-verify pytest ruff pre-commit -y
* Remove Environment: conda remove -n anaconda_package --all -y
* Activate Environment conda activate anaconda_package
* Deactivate Environment conda deactivate
* Documentation: pip install .[docs]
* Pip build: pip install build

### Build
* Purge: conda build purge-all
* Conda Build: conda build conda-recipe
* Pip Build: python -m build

### Install
* Install: conda install --use-local gregs_conda_package -n anaconda_package -y
* Uninstall: conda remove gregs_conda_package -n anaconda_package -y

### Checks
* Style: ruff format .
* Lint: ruff check . --fix
* Pre-commit check: pre-commit run --all-files
* Test: pytest -v
* Document: mkdocs build --strict

# Github Actions

* Build documents on PR and merge into main.
* Ensure code follows lint rules & well formated on PR and merge into main.
* Confirm package could be published to pypi on PR and merge into main.
* Run tests on linux, mac, and windows on push and PR.
* Build conda package on PR and merge into main.


