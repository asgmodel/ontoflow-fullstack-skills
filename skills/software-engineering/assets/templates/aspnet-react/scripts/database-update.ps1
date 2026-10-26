$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$project = Join-Path $root "src/App.Server/App.Server.csproj"

Push-Location (Split-Path -Parent $project)
try {
  dotnet ef database update `
    --project $project `
    --startup-project $project `
    --context AppDbContext
  if ($LASTEXITCODE -ne 0) { throw "EF command failed with exit code $LASTEXITCODE" }
} finally {
  Pop-Location
}
