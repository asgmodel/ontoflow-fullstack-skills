param(
  [Parameter(Mandatory = $true)]
  [ValidatePattern('^[A-Za-z][A-Za-z0-9_]*$')]
  [string]$Name
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$project = Join-Path $root "src/App.Server/App.Server.csproj"

Push-Location (Split-Path -Parent $project)
try {
  dotnet ef migrations add $Name `
    --project $project `
    --startup-project $project `
    --context AppDbContext `
    --output-dir Infrastructure/Data/Migrations
  if ($LASTEXITCODE -ne 0) { throw "EF command failed with exit code $LASTEXITCODE" }
} finally {
  Pop-Location
}
