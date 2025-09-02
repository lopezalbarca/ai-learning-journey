#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt

echo "Env ready. Activate with: source .venv/bin/activate"
