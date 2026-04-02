#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# set +e so bash 5.x -e flag does not exit silently on example.sh failure
set +e
output=$(bash "$SCRIPT_DIR/example.sh" 2>&1)
status=$?
set -e

if [ $status -ne 0 ]; then
  echo "FAIL: example.sh exited with status $status"
  echo "$output"
  exit 1
fi

if [ -z "$output" ]; then
  echo "FAIL: example.sh produced no output"
  exit 1
fi

echo "PASS"
echo "$output" | head -3