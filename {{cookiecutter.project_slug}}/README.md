# {{ cookiecutter.project_name }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug}}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)


---

**Source Code**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
**PyPI**: [https://pypi.org/project/{{ cookiecutter.project_slug }}/](https://pypi.org/project/{{ cookiecutter.project_slug }}/)

---

{{ cookiecutter.project_short_description }}

## Installation

```sh
pip install {{ cookiecutter.project_slug }}
```

## Development

This project requires at Python 3.9+ and uses
[Poetry](https://python-poetry.org/) to manage dependencies.

Once you've created and activated your virtual environment, run:

```sh
poetry install
```

This will install all necessary dependencies and install this project
in editable mode.


### Testing

[Poe the Poet](https://github.com/nat-n/poethepoet) is the task runner
used for this project, it's automatically installed as part of the
`poetry install` step.  To see a list of available tasks, run the
`poe` command with no args.

To run the tests for this project run:


```sh
poe test
```

Before submitting a PR, ensure the `prcheck` task runs successfully:

```sh
poe prcheck
```
