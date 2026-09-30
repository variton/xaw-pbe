#! /bin/bash

curl --fail-with-body -i \
  -X POST http://127.0.0.1:7777/api/login/ \
  -H 'Content-Type: application/json' \
  -d '{"email":"morpheus@matrix.com","pwd":"1234"}'
