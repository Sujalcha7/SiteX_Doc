# Clean LaTeX auxiliary files and recompile
$docDir = Get-Location
$mainFile = "main"

Write-Host "Cleaning old compilation files..." -ForegroundColor Yellow

# Remove auxiliary files
Remove-Item -Path "$docDir\*.aux" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\*.log" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\*.out" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\*.toc" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\*.lof" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\*.lot" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\*.fls" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\*.fdb_latexmk" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\*.bbl" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\*.blg" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\chapter\*.aux" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$docDir\main.pdf" -Force -ErrorAction SilentlyContinue

Write-Host "Recompiling document..." -ForegroundColor Cyan

# First pass - redirect input from nul to prevent hanging
Write-Host "Pass 1/4: Initial LaTeX run..."
cmd /c "xelatex -halt-on-error -interaction=batchmode $mainFile.tex < nul > nul 2>&1"

# BibTeX pass (only if aux exists and has bibliography data)
Write-Host "Pass 2/4: Processing bibliography..."
$auxPath = Join-Path $docDir "$mainFile.aux"
if (Test-Path $auxPath) {
    $auxContent = Get-Content $auxPath -ErrorAction SilentlyContinue
    if ($auxContent -match "\\bibdata" -and $auxContent -match "\\bibstyle") {
        cmd /c "bibtex $mainFile.aux"
    } else {
        Write-Host "Skipping BibTeX: no \\bibdata/\\bibstyle in main.aux" -ForegroundColor Yellow
    }
} else {
    Write-Host "Skipping BibTeX: main.aux not found (LaTeX likely failed)" -ForegroundColor Yellow
}

# Second pass
Write-Host "Pass 3/4: Updating TOC and references..."
cmd /c "xelatex -halt-on-error -interaction=batchmode $mainFile.tex < nul > nul 2>&1"

# Third pass
Write-Host "Pass 4/4: Final pass for reference resolution..."
cmd /c "xelatex -halt-on-error -interaction=batchmode $mainFile.tex < nul > nul 2>&1"

Write-Host ""
if (Test-Path "$docDir\main.pdf") {
    $pdfSize = (Get-Item "$docDir\main.pdf").Length / 1MB
    Write-Host "SUCCESS: PDF generated!" -ForegroundColor Green
    Write-Host "File: main.pdf (Size: $('{0:F2}' -f $pdfSize) MB)" -ForegroundColor Cyan
} else {
    Write-Host "FAILED: PDF was not generated." -ForegroundColor Red
    Write-Host "Checking log file for errors..." -ForegroundColor Yellow
    if (Test-Path "$docDir\main.log") {
        Write-Host ""
        Get-Content "$docDir\main.log" | Select-String -Pattern "Error|error|ERROR" | Select-Object -First 10
    }
}
