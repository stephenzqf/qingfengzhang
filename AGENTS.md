# AGENTS.md — CV Project (Zhang Qingfeng)

## Project Overview

This is a personal Curriculum Vitae (CV) project for **Zhang Qingfeng** (张庆峰), a PhD candidate in Water Resources and Hydropower Engineering at Wuhan University. The project maintains his CV in multiple output formats (LaTeX/PDF and Word/DOCX), submission cover letters, a personal academic website, and a small utility for extracting text from award certificate PDFs.

## Directory Structure

```
cv-master/
├── CV/
│   ├── latex/                              # LaTeX source and build artifacts
│   │   ├── cv-Zhang Qingfeng_260608.tex    # Main CV source (XeLaTeX)
│   │   ├── cv-Zhang Qingfeng_260608.pdf    # Compiled PDF output
│   │   ├── cv-Zhang Qingfeng_260608.aux    # LaTeX auxiliary (toc/bookmarks)
│   │   ├── cv-Zhang Qingfeng_260608.out    # LaTeX hyperref bookmarks
│   │   └── cv-Zhang Qingfeng_260608.log    # Compilation log
│   ├── paper/                              # Submission cover letters (PDF)
│   │   ├── Cover Letter.pdf                # Science Advances (2026-03-28)
│   │   ├── cover_letter.pdf                # ACP (2026-05-29)
│   │   └── npj.pdf                         # npj Urban Sustainability (2026-05-22)
│   ├── cv-Zhang Qingfeng_260101.docx       # Earlier DOCX version (2026-01-01)
│   ├── cv-Zhang Qingfeng_260608.docx       # DOCX version (2026-06-08, regenerated via pandoc)
│   └── cv-Zhang Qingfeng_260608.pdf        # Latest PDF version
├── Website/                                # Personal academic website
│   ├── index.html                          # Single-page site (all CV sections)
│   └── styles.css                          # Styles (blue academic theme)
├── extract_cert.py                         # Python script: extract text from certificate PDFs (CLI arg)
├── cert_text.txt                           # Sample output from extract_cert.py
└── AGENTS.md                               # This file
```

## File Naming Convention

All CV files follow the pattern: `cv-Zhang Qingfeng_YYMMDD.ext`

- `260101` = 2026-01-01 (earlier DOCX version)
- `260608` = 2026-06-08 (latest version, date of last LaTeX compilation per the log file)

When updating the CV: rename the `.tex` file to the new date, recompile twice with XeLaTeX, regenerate the DOCX via pandoc, and copy the PDF to `CV/`.

## Technology Stack

### LaTeX / XeLaTeX

- **Compiler**: XeLaTeX (required — uses `fontspec` for system fonts)
- **TeX Distribution**: TeX Live 2025
- **Key Packages Used**:
  - `geometry` — page margins (0.50in top, 0.35in bottom, 0.65in left/right)
  - `fontspec` — system font loading (Times New Roman for body, Arial for sans-serif)
  - `titlesec` — custom section heading formatting
  - `enumitem` — compact list styling with `--` bullets
  - `hyperref` — PDF hyperlinks and metadata
  - `xcolor` — custom colors (`sectioncolor` RGB 30,60,120)
  - `fontawesome5` — email icon in header
- **Document class**: `article`, 10pt, A4 paper
- **Output**: 2-page PDF

### Website

- Plain static HTML5 + CSS3, no JavaScript, no build step. Single page with anchor navigation.
- Sections: About, Education, Research Interests, Publications, Conferences, Research Experience, Awards, Skills, Contact.
- Responsive design (breakpoints 992px / 768px / 576px). Deployed via GitHub Pages.

### Python

- **Runtime**: Python 3.12
- **Dependency**: `PyPDF2` (used in `extract_cert.py`)
- No `requirements.txt`, `pyproject.toml`, or virtual environment setup exists.

## Build and Test Commands

### Compile the CV (LaTeX → PDF)

```bash
# From within CV/latex directory
cd CV/latex
xelatex "cv-Zhang Qingfeng_260608.tex"

# To ensure bookmarks resolve correctly (from .out), run twice:
xelatex "cv-Zhang Qingfeng_260608.tex"
xelatex "cv-Zhang Qingfeng_260608.tex"
```

The first comment line (`% !TEX program = xelatex`) serves as a directive for editors like TeXstudio to auto-select the XeLaTeX compiler.

### Regenerate the DOCX (LaTeX → Word)

```bash
pandoc "CV/latex/cv-Zhang Qingfeng_260608.tex" -o "CV/cv-Zhang Qingfeng_260608.docx" --from latex
```

Note: pandoc does not render `fontawesome5` icons; the email line in the DOCX may show a placeholder glyph. Manual cleanup in Word may be needed.

### Run the Certificate Extraction Script

```bash
python extract_cert.py <path-to-certificate.pdf>
```

The script takes the PDF path as a CLI argument (no more hardcoded path) and prints each page's text with UTF-8 output.

## CV Content Sections

The CV is organized into the following sections (in order):

1. **Header** — Name, email (with Font Awesome envelope icon)
2. **Education Background** — PhD at Wuhan University (2024–Now, supervisor Prof. Jiyun Song), B.Eng. at Northwest A&F University (2020–2024, supervisor Prof. Yi Li)
3. **Research Interests** — 3 items (urban climate dynamics; physics-informed spatiotemporal deep learning; climate-just urban informatics)
4. **Journal Publications** — 2 published (Building and Environment 2026; Water 2022) + 3 submitted/under review (ACP, npj Urban Sustainability, Science Advances)
5. **Conference Presentations** — 11 presentations (EGU 2026 ×2, ICUC12 ×2, AOGS 2025 ×2, etc.)
6. **Research & Project Experience** — 4 projects (PhD research: causal ML / HyperClim-Former / STGNN nowcasting; Yellow River Basin; Robot Vision; Water Platform)
7. **Competition Awards** — 12 awards (robotics, water resources, mathematical modeling, etc.)
8. **Skills** — HPC/WRF, AI/Deep Learning, Scientific Programming, Geospatial Analysis, Languages

## Custom LaTeX Commands

The `.tex` file defines two convenience commands:

- `\cvitembf{label}{text}` — An `\item` with bold label (used in Skills section)
- `\cventry{number}{text}` — A numbered `\item` with bold number (not currently used)

## Code Style Guidelines

### LaTeX

- The `.tex` file uses single-line commenting (no block comments) with `% === SECTION NAME ===` style section dividers.
- Indentation: consistent 4-space indent within environments.
- The file encoding is UTF-8 (required for XeLaTeX with `fontspec`).
- Line endings: LF (Unix-style), though the environment is Windows.
- When editing: **do not change the `% !TEX program = xelatex` magic comment** on line 1.

### Python

- `extract_cert.py` uses a flat procedural style with no function definitions. Keep it simple.
- Line endings: LF. Output is UTF-8 via `sys.stdout.reconfigure`.
- Basic error handling: missing argument, unreadable PDF, per-page extraction errors.

### Website

- Content is authored in `index.html` directly; `styles.css` holds all styling. No templates or generators.
- **Keep the website in sync with the LaTeX CV** — the LaTeX source is the authoritative content source. When the CV changes, update the site sections (publications, conferences, awards) to match.

## Security Considerations

- The CV contains personal information (email, academic history, awards). Keep `AGENTS.md` general — do not duplicate sensitive content in this file.
- No credentials or secrets are present in this repository. Do not commit tokens or absolute local paths.

## Notes

- There is **no build automation**, **no CI/CD**, and **no test suite** — this is a simple document project.
- The LaTeX source is the authoritative version for the latest CV (260608). DOCX is regenerated via pandoc; the website mirrors the same content.
- The `CV/latex/` directory contains build artifacts (`.aux`, `.log`, `.out`) that are regenerated on each compilation and do not need to be version-controlled, though they are currently tracked in the repository.
- The website is deployed to GitHub Pages from this repository's `Website/` folder.
