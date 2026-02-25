#!/bin/bash
set -e
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
rm -rf "$ROOT_DIR/dist"
python -m pip install -q build
(cd "$ROOT_DIR" && python -m build)
