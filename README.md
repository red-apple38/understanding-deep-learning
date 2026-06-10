# Understand Deep Learning

A didactic deep learning course built around executable Jupyter notebooks, reusable
Python modules, tests, and a Quarto book.

The notebooks intentionally introduce concepts step by step. Code may remain
notebook-specific while it is educationally useful; reusable implementations are
gradually generalized and moved into `src/`.

## Repository Structure

- `docs/`: course notebooks and documentation assets
- `src/`: reusable Python modules extracted from the course material
- `tests/`: automated tests for reusable modules
- `site/`: generated Quarto output
- `.github/workflows/`: continuous integration and GitHub Pages deployment
- `_quarto.yml`: Quarto book configuration
- `pyproject.toml`: package metadata, dependencies, and tool configuration
- `requirements.txt`: convenience entry point for an editable development install

## Requirements

- Python 3.11 or newer
- Quarto 1.8 or compatible
- Git
- Docker, optionally

Install Quarto from the
[official installation guide](https://quarto.org/docs/get-started/).

## Local Setup

Create and activate a virtual environment from the repository root.

### Windows PowerShell

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS or Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The requirements file installs the repository in editable mode with the course and
development dependency groups defined in `pyproject.toml`.

The optional `.env.example` documents the source-path fallback used by some IDEs.
An editable installation should normally make `PYTHONPATH` configuration unnecessary.

## Running the Notebooks

Start JupyterLab from the repository root:

```bash
jupyter lab
```

Open notebooks from `docs/` and select the Python environment in which the project
was installed.

## Quarto Book

Preview the course website locally:

```bash
quarto preview
```

Render the HTML site:

```bash
quarto render --to html
```

Generated output is written to `site/`, as configured in `_quarto.yml`.

## Running Tests

```bash
python -m pytest
```

The development dependencies include `pytest` and `pytest-mock`.

## Docker

Build the image:

```bash
docker build -t understand-deep-learning .
```

Open an interactive shell:

```bash
docker run --rm -it understand-deep-learning
```

Run JupyterLab while mounting the repository on Windows PowerShell:

```powershell
docker run --rm -it -p 8888:8888 -v "${PWD}:/app" understand-deep-learning `
  jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

On macOS or Linux, replace `${PWD}` with `$(pwd)`.

Render the Quarto site inside Docker:

```powershell
docker run --rm -it -v "${PWD}:/app" understand-deep-learning quarto render --to html
```

## Development Workflow

1. Introduce concepts and notebook-specific implementations in `docs/`.
2. Move code into `src/` when it becomes reusable across lessons.
3. Add behavioral tests under `tests/`.
4. Run the tests and render the Quarto book before submitting changes.
5. Keep generated files, local environments, credentials, and caches out of new commits.

`pyproject.toml` is the canonical dependency source. Update its dependency groups
instead of maintaining a separate duplicated package list.

Formatting enforcement is intentionally deferred during the first cleanup phase
because existing source and test formatting is outside its scope. A later phase can
format those files and restore the Black CI check.

## Generated Output

Quarto output under `site/` is ignored for future generation. Files already tracked
there are intentionally left untouched during the first cleanup phase.

## License

See [LICENSE](LICENSE).
