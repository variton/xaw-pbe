# XAW Python Backend

Python backend for XAW, using FastAPI and Pydantic. The application currently
provides heartbeat and development login endpoints.

## Requirements

- Python 3.10 or newer (below 4.0)
- [uv](https://docs.astral.sh/uv/) for dependency management

## Get started

From the project directory, create the environment and install dependencies:

```bash
uv sync
```

uv creates a `.venv` and installs dependencies without packaging the backend,
whose application entry point is `src/xawpbe.py` with routers in `src/routes/`.
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

The backend is available at `http://127.0.0.1:7777`. Interactive API
documentation is served at `/docs` and `/redoc`, with the OpenAPI schema at
`/openapi.json`.

Browser requests are configured to allow the frontend origin
`http://localhost:5173`, including credentials and GET/POST methods. The CORS
configuration lives in `src/xawpbe.py`.

## API endpoints

| Method | Path | Behavior |
| --- | --- | --- |
| GET | `/api/hbeat/` | Returns HTTP 200 with `{"hbeat":"ok"}`. |
| POST | `/api/login/` | Accepts JSON fields `email` and `pwd`; returns HTTP 200 with `{"ok":true}` for the development credentials. |

Check the heartbeat:

```bash
curl http://127.0.0.1:7777/api/hbeat/
```

Log in with the development credentials and save the response cookie:

```bash
curl -c /tmp/xaw-cookies.txt \
  -H 'Content-Type: application/json' \
  -d '{"email":"morpheus@matrix.com","pwd":"1234"}' \
  http://127.0.0.1:7777/api/login/
```

Invalid credentials return HTTP 401. Missing required fields or a missing JSON
body return HTTP 422. Credentials must be supplied in the JSON body.

Login currently uses hardcoded credentials and a fixed token for local
development. A successful login sets an `access_token` cookie with `HttpOnly`,
`SameSite=lax`, and path `/`. Its `Secure` flag is disabled for local HTTP;
production authentication and HTTPS cookie settings must be implemented before
using this login flow in production.

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
