# Python Package Update Monitor

This tool checks your installed Python packages and compares them to the latest versions on PyPI.

## Features

- Lists all installed packages and their status (up to date or outdated).
- Optionally shows only outdated packages.
- Save results to a file.
- Exclude specified packages from checking.

## Usage

Run:

```bash
python3 monitor.py

Options:

--outdated-only: show only outdated packages.
--save FILE: save output to FILE.
--exclude PKG1 PKG2... exclude listed packages.
