#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
ROOT_DIR=$(cd "$SCRIPT_DIR/.." && pwd)

python3 -m venv "$ROOT_DIR/.venv"
source "$ROOT_DIR/.venv/bin/activate"

pip install --upgrade pip
pip install -r "$SCRIPT_DIR/requirements.base.txt"
pip install jupyter

pip freeze > "$SCRIPT_DIR/requirements.txt"

echo "✅ Setup complete. Activate venv with: source .venv/bin/activate"
