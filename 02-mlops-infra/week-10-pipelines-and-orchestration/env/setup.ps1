Param()

python -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt

Write-Host "Env ready. Activate with: .\.venv\Scripts\Activate.ps1"
