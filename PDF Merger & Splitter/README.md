# Python Desktop Scripts

A small collection of Python scripts for everyday desktop tasks.

## Description

| Script | What it does | Docs |
| --- | --- | --- |
| `pdf_merger.py` | Merges selected pages from several PDFs into a single PDF | [pdf_merger.md](pdf_merger.md) |
| `pdf_splitter.py` | Splits one PDF into three PDFs by page ranges | [pdf_splitter.md](pdf_splitter.md) |

Each script is a short, edit-and-run file: change the settings at the top, then run it.

## Compatibility

- **Python:** 3.6 or newer
- **Dependency:** [PyPDF2](https://pypi.org/project/PyPDF2/) **older than 3.0** (for example `2.12.1`), because the scripts use the legacy `PdfFileMerger`, `PdfFileReader` and `PdfFileWriter` classes, which were removed in PyPDF2 3.0
- **OS:** Windows, macOS and Linux

```bash
pip install "PyPDF2<3.0"
```

## Settings

Both scripts are configured by editing values directly in the file. There are no command-line options or config files.

### PDF Merger (`pdf_merger.py`)

| Setting | Where | Description |
| --- | --- | --- |
| Input files | `merger.append("PDF1_FILENAME.pdf", ...)` | Path of each PDF to merge, merged in the order listed. Add or remove `append` lines to merge more or fewer files. |
| Page selection | `pages=(0,0)` | A `(start, stop)` tuple of zero-based page indexes, where `stop` is not included. For example, `pages=(0, 3)` takes the first three pages. Omit `pages=` to include every page. |
| Output file | `merger.write("MERGED_PDF_FILENAME.pdf")` | Name of the merged PDF to create. |

> **Note:** the placeholder `pages=(0,0)` selects no pages. Replace it with a real range before running.

### PDF Splitter (`pdf_splitter.py`)

| Setting | Where | Description |
| --- | --- | --- |
| Page groups | `PDF1_FILENAME`, `PDF2_FILENAME`, `PDF3_FILENAME` (top of the file) | Lists of zero-based page indexes for each output. Example: `list(range(0, 7))` for the first seven pages, or `[4, 7]` for specific pages. |
| Input file | `open("PDF_FILENAME.pdf", ...)` | The PDF to split. |
| Output files | `open("PDF1_FILENAME.pdf", "wb")`, etc. | Names of the three PDFs to create. |

See [pdf_merger.md](pdf_merger.md) and [pdf_splitter.md](pdf_splitter.md) for per-script details.
