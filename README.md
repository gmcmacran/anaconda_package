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

* Conda Environment: conda create -n anaconda_package python=3.13.5 conda-verify pytest ruff pre-commit -y
* Remove Environment: conda remove -n anaconda_package --all -y
* Activate Environment conda activate anaconda_package
* Deactivate Environment conda deactivate
* Documentation: pip install .[docs]

* Purge: conda build purge-all
* Build: conda build conda-recipe

* Install: conda install --use-local gregs_conda_package -n anaconda_package -y
* Uninstall: conda remove gregs_conda_package -n anaconda_package -y

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


