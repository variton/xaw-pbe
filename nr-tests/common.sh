#!/bin/bash

# Usage: assert_response EXPECTED_STATUS EXPECTED_JSON curl [arguments...]
# The command must support curl's --write-out option.
assert_response() {
    local expected_status="$1" expected_json="$2"
    shift 2
    local output actual_status body

    if ! output=$("$@" --silent --show-error --max-time 30 --write-out $'\n%{http_code}'); then
        printf 'ERROR: request command failed\n' >&2
        return 1
    fi

    actual_status="${output##*$'\n'}"
    body="${output%$'\n'*}"
    if [[ "$actual_status" != "$expected_status" ]]; then
        printf 'ERROR: expected HTTP %s, got %s; body: %s\n' \
            "$expected_status" "$actual_status" "$body" >&2
        return 1
    fi

    if ! python3 - "$expected_json" "$body" <<'PY'
import json
import sys

try:
    expected, actual = (json.loads(value) for value in sys.argv[1:])
except ValueError as error:
    print(f"ERROR: invalid JSON response or expectation: {error}", file=sys.stderr)
    sys.exit(1)

if json.dumps(actual, sort_keys=True) != json.dumps(expected, sort_keys=True):
    print(f"ERROR: expected {expected!r}, got {actual!r}", file=sys.stderr)
    sys.exit(1)
PY
    then
        return 1
    fi

    printf 'OK: HTTP %s, body: %s\n' "$actual_status" "$body"
}
