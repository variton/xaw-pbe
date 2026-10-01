#! /bin/bash

source "$(dirname "${BASH_SOURCE[0]}")/common.sh"

assert_response 200 '{"ok":true}' curl \
  -X POST "${BASE_URL:-http://127.0.0.1:7777}/api/login/" \
  -H 'Content-Type: application/json' \
  -d '{"email":"morpheus@matrix.com","pwd":"1234"}'
