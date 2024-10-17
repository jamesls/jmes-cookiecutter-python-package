# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Installation

```sh
pip install {{ cookiecutter.project_slug }}
```

## Development

This project requires Python 3.12 and uses
[uv](https://github.com/astral-sh/uv) to manage dependencies.

You can create a virtual environment with all the necessary dependencies
by running:

```sh
uv sync --all-extras --dev
```

This will install all necessary dependencies and install this project
in editable mode.

You can activate the venv with:

```sh
. .venv/bin/activate
```

### Testing

[Poe the Poet](https://github.com/nat-n/poethepoet) is the task runner
used for this project, it's automatically installed as part of the
dev dependencies.  To see a list of available tasks, run the
`poe` command with no args.

To run the tests for this project run:


```sh
poe test
```

Before submitting a PR, ensure the `prcheck` task runs successfully:

```sh
poe prcheck
```
