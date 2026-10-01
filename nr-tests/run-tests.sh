#!/bin/bash

test_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)" || exit 1
shopt -s nullglob
tests=("$test_dir"/test-*.sh)

if (( ${#tests[@]} == 0 )); then
    printf 'ERROR: no test scripts found in %s\n' "$test_dir" >&2
    exit 1
fi

for test_script in "${tests[@]}"; do
    printf 'Running %s\n' "${test_script##*/}"
    bash "$test_script"
    result=$?
    if (( result != 0 )); then
        printf 'ERROR: %s failed (exit code %s); stopping tests\n' \
            "${test_script##*/}" "$result" >&2
        exit "$result"
    fi
done

printf 'All tests passed\n'
