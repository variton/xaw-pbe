# Shell API tests

These tests require Bash, curl, Python 3, and a running backend. From the
project directory, start the backend in one terminal:

```bash
uv run uvicorn xawpbe:app --app-dir src --host 127.0.0.1 --port 7777
```

Run all tests in another terminal:

```bash
BASE_URL=http://127.0.0.1:7777 bash nr-tests/run-tests.sh
```

The runner executes every `test-*.sh` script in filename order and stops at
the first failure, printing an error and returning the failed test's exit code.
It exits with code 0 and prints `All tests passed` when all tests succeed.
If no test scripts are found, it prints an error and exits with code 1.
The runner locates tests relative to itself, so it also works when invoked
by its absolute path from another working directory.

To run individual tests:

```bash
BASE_URL=http://127.0.0.1:7777 bash nr-tests/test-hbeat.sh
BASE_URL=http://127.0.0.1:7777 bash nr-tests/test-login.sh
```

Set `BASE_URL` to the backend address, without a trailing slash. Without it,
`test-hbeat.sh` uses `http://127.0.0.1:8000` and `test-login.sh` uses
`http://127.0.0.1:7777`.
The shared `assert_response` function in `common.sh` executes curl and checks
the HTTP status and JSON body. It prints an error to stderr and returns exit
code 1 for a failed command, unexpected status, invalid JSON, or incorrect body.
Requests time out after 30 seconds. JSON comparison ignores object key order
and formatting but checks the complete response, including value types.

## Add a test

Create a `test-*.sh` file in this directory. Source `common.sh` relative to the
script and call `assert_response` with the expected status, expected JSON,
and curl command:

```bash
#!/bin/bash
source "$(dirname "${BASH_SOURCE[0]}")/common.sh"

assert_response 200 '{"hbeat":"ok"}' curl \
  -L "${BASE_URL:-http://127.0.0.1:7777}/api/hbeat"
```

The runner discovers the new script automatically. Keep the assertion as the
last command, or explicitly propagate its failure with `|| exit 1` if the
script performs additional commands. Do not add curl's `-i` option: the helper
expects the response body without HTTP headers.
