# XAW Python Backend

Python backend for XAW, using FastAPI and Pydantic.

## Requirements

- Python 3.14 (as specified in `pyproject.toml`)
- Poetry for dependency management

## Get started

From the project directory, create the environment and install dependencies:

```bash
poetry env use python3.14
poetry install --no-root
```

The `--no-root` option installs dependencies without installing this project as a
package, since the repository does not yet contain application code.

Check that FastAPI imports successfully:

```bash
poetry run python -c "import fastapi; print(fastapi.__version__)"
```

## Current status

This repository currently contains dependency configuration only. There is no
application entry point, server command, or test suite yet. Add the backend code
before starting a server.

Dependencies are declared in `pyproject.toml`. Run Python commands inside the
managed environment with `poetry run <command>`.
