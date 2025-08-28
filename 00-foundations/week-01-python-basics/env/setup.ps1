Param(
    [switch]$Recreate
)
$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$rootDir = Join-Path $scriptDir '..'
$venvPath = Join-Path $rootDir '.venv'

if ($Recreate -and (Test-Path $venvPath)) { Remove-Item -Recurse -Force $venvPath }

python -m venv $venvPath
& "$venvPath/Scripts/Activate.ps1"

python -m pip install --upgrade pip
pip install -r (Join-Path $scriptDir 'requirements.base.txt')
pip install jupyter

pip freeze | Out-File -FilePath (Join-Path $scriptDir 'requirements.txt') -Encoding ascii

Write-Host '✅ Setup complete. Activate venv with: .\.venv\Scripts\Activate.ps1'
