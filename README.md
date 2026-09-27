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

## Current status

The initial FastAPI application is in `src/xaw-pbe.py`. It still needs a
`CORSMiddleware` import before it can start. There is no test suite yet.

Dependencies are declared in `pyproject.toml`. Run Python commands inside the
managed environment with `uv run <command>`. Commit `uv.lock` to keep dependency
versions reproducible; use `uv sync --locked` in CI.
