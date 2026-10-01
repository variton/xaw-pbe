# XAW Python Backend

Python backend for XAW, using FastAPI and Pydantic.

## Requirements

- Python 3.10 or newer (below 4.0)
- [uv](https://docs.astral.sh/uv/) for dependency management

## Get started

From the project directory, create the environment and install dependencies:

```bash
uv sync
```

uv creates a `.venv` and installs dependencies without packaging the backend,
which is currently a standalone script in `src/`.
Development and CI tools are included by default. To install only runtime
dependencies, use `uv sync --no-dev`. To include documentation
tools, use `uv sync --group docs`.

Check that FastAPI imports successfully:

```bash
uv run python -c "import fastapi; print(fastapi.__version__)"
```

## Run the backend

Start the FastAPI application from the project directory:

```bash
uv run uvicorn xawpbe:app --app-dir src --host 127.0.0.1 --port 7777
```

## Run tests

Run the Python endpoint tests:

```bash
PYTHONPATH=src uv run pytest
```

With the backend running, execute all shell tests in a separate terminal:

```bash
BASE_URL=http://127.0.0.1:7777 bash nr-tests/run-tests.sh
```

The runner discovers `test-*.sh` scripts in `nr-tests` and executes them in
filename order. Each test checks the HTTP status and JSON response body.
If a test fails, the runner prints an error, stops immediately, and exits with
that test's nonzero exit code. It prints `All tests passed` and exits with code
0 when every test succeeds. An empty test directory produces exit code 1.

Shell tests require Bash, curl, and Python 3. Set `BASE_URL` to the backend
address so every test uses the same server. See [the shell test documentation](nr-tests/README.md)
for individual test commands and instructions for adding tests.

## Dependency management

Dependencies are declared in `pyproject.toml`. Run Python commands inside the
managed environment with `uv run <command>`. Commit `uv.lock` to keep dependency
versions reproducible; use `uv sync --locked` in CI.
