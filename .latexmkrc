# Force latexmk to use XeLaTeX for PDF generation
$pdf_mode = 1;  # generate PDF
# Use xelatex as the pdflatex command
$pdflatex = 'xelatex -interaction=nonstopmode -synctex=1 %O %S';
# Ensure latexmk knows about xelatex target
$xelatex = $pdflatex;
# Don't stop on warnings
$failure_cmd = '';
# Save log of latexmk
$logfile = "latexmkrc.log";
