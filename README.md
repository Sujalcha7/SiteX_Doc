# SiteX_Doc

Documentation for project SiteX.

---

## Overview

This repository contains the documentation for the SiteX project, structured according to standard academic and technical report conventions. All chapters and sections are implemented in LaTeX.

## Table of Contents

- [Front page](#)
- [Certification](#)
- [Acknowledgement](#)
- [Table of Content](#)
- [Abstract](#)
- [List of Figures](#)
- [List of Tables](#)
- [List of Abbreviation](#)
- [Appendix](#)
- [Bibliography](#)
  
## How to Build the Document

The documentation uses LaTeX. Follow the instructions for your operating system to compile the project and generate the PDF.

### 1. Prerequisites

Before building the document, ensure you have the following:

- All `.tex` source files (typically `main.tex` or similar entrypoint)
- Any custom style files (`.sty`), bibliography files (`.bib`), images, etc.

---

### 2. Compiling on **Windows**

#### Option A: Using [MiKTeX](https://miktex.org/)

1. **Install MiKTeX:**
   - Download the MiKTeX installer from [here](https://miktex.org/download).
   - Run the installer and follow the instructions.

2. **Install a LaTeX Editor (Recommended: TeXworks, TeXstudio, or Overleaf Desktop):**
   - TeXworks comes bundled with MiKTeX.
   - Alternatively, download TeXstudio from [here](https://www.texstudio.org/).

3. **Compile the Document:**
   - Open your main `.tex` file (e.g., `main.tex`) in your editor.
   - Click "Compile" (usually with "pdfLaTeX" or "XeLaTeX").
   - Alternatively, open a command prompt in your project directory and run:
     ```
     pdflatex main.tex
     bibtex main
     pdflatex main.tex
     pdflatex main.tex
     ```
   - The output will be `main.pdf` in the same directory.

#### Option B: Using [Overleaf](https://overleaf.com/)

- Upload all files to a new Overleaf project.
- Click "Recompile" to build the PDF.

---

### 3. Compiling on **Linux**

#### Option A: Using TeX Live

1. **Install TeX Live:**

   - Ubuntu/Debian:
     ```
     sudo apt update
     sudo apt install texlive-full
     ```

   - Fedora:
     ```
     sudo dnf install texlive-scheme-full
     ```

2. **Compile the Document:**

   - Open a terminal in your project directory.
   - Run:
     ```
     pdflatex main.tex
     bibtex main
     pdflatex main.tex
     pdflatex main.tex
     ```

   - The PDF `main.pdf` will be generated.

#### Option B: Using Overleaf (Web-based, see above)

---

### 4. Notes & Troubleshooting

- Replace `main.tex` with your actual entrypoint if different.
- Run `pdflatex` multiple times if you have cross-references, TOC, bibliography, or list of figures/tables.
- If you encounter missing packages, MiKTeX and TeX Live can install them automatically (if prompted).
- For graphics, ensure all image paths are correct and files are present.

---

## Contribution

Feel free to open issues or pull requests to improve the documentation.

## License

See [LICENSE](LICENSE) for details.
