# SpoTex_Doc

Documentation for project SpoTex.

---

## Overview

This repository contains the documentation for the SpoTex project, structured according to standard academic and technical report conventions. All chapters and sections are implemented in LaTeX.

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

### Chapters Included

- Chapter 1: Introduction
    - Background Introduction
    - Motivation
    - Problem Definition
    - Goals and Objective
    - Scope and Application
    - Report Organization
- Chapter 2: Literature Review
    - Deep-Sort/nwokje
    - Deep SORT and YOLO v4 for people tracking and detection with Tensorflow backend/ LeonLok
    - Multi-Camera Live Object Tracking
    - YOLOv4: Optimal Speed and Accuracy of Object Detection
    - Maximum correntropy Kalman filter
- Chapter 3: Feasibility Study
    - Technical Feasibility
    - Operational Feasibility
    - Economic Feasibility
    - Scheduling Feasibility
- Chapter 4: Methodology
- Chapter 5: Requirement Analysis
    - Software Requirement
    - Hardware Requirement
    - Functional Requirement
    - Non-Functional Requirement
- Chapter 6: System Design and Architecture
    - Use Case Diagram
    - Context Diagram
    - Data Flow Diagram
    - Sequence Diagram
    - Schedule (Gantt Chart)
    - Cost Estimation
- Chapter 7: Block Diagram and Description of Proposed System
    - System Block Diagram
    - YOLO
    - Darknet
    - Intersection Over Union
    - Non-Maximum Suppression
    - COCO dataset
    - Kalman Filter in Deepsort
    - Python Text To Speech
- Chapter 8: Expected Outcome
- Chapter 9: Actual Outcome
- Chapter 10: Conclusion and Recommendation
- References

---

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
