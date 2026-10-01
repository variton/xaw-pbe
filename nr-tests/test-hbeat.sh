#! /bin/bash

source "$(dirname "${BASH_SOURCE[0]}")/common.sh"

assert_response 200 '{"hbeat":"ok"}' curl \
  -L "${BASE_URL:-http://127.0.0.1:8000}/api/hbeat"
