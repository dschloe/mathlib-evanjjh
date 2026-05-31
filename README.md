# mathlib-evanjjh

A lightweight, class-based Python utility library for basic arithmetic operations. This package was created for **educational purposes** to demonstrate Python project structure, testing, packaging, and PyPI distribution.

**PyPI:** [https://pypi.org/project/mathlib-evanjjh/](https://pypi.org/project/mathlib-evanjjh/)

> The package description mentions geometric sequences and trigonometry as future scope. The current release (`0.1.1`) ships the `Arithmetic` class only.

## Features

- **Class-based API** — Store two operands in an `Arithmetic` instance and call methods for each operation.
- **Basic operations** — Addition, subtraction, multiplication, and division.
- **Safe division** — Raises `ValueError` when dividing by zero.
- **Zero runtime dependencies** — Works with Python 3.8+ only.
- **Tested** — Unit tests with pytest.

## Requirements

- Python **3.8** or newer (development uses Python 3.13)

## Installation

### From PyPI

```bash
pip install mathlib-evanjjh
```

### From source

```bash
git clone https://github.com/dschloe/mathlib-evanjjh.git
cd mathlib-evanjjh
pip install -e .
```

With [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Quick Start

```python
from mathlib_evanjjh.arithmetic import Arithmetic

calc = Arithmetic(10, 3)

print(calc.add())       # 13
print(calc.subtract())  # 7
print(calc.multiply())  # 30
print(calc.divide())    # 3.333...
```

### Division by zero

```python
Arithmetic(5, 0).divide()  # raises ValueError
```

## API Reference

### `Arithmetic(a, b)`

Create an instance with two numeric operands `a` and `b`.

| Method        | Description     | Returns          |
|---------------|-----------------|------------------|
| `add()`       | Returns `a + b` | `int` or `float` |
| `subtract()`  | Returns `a - b` | `int` or `float` |
| `multiply()`  | Returns `a * b` | `int` or `float` |
| `divide()`    | Returns `a / b` | `float`          |

**Raises**

- `ValueError` — When `b` is `0` in `divide()`.

## Project Structure

```
mathlib-evanjjh/
├── src/
│   └── mathlib_evanjjh/
│       ├── __init__.py
│       └── arithmetic.py    # Arithmetic class
├── tests/
│   ├── __init__.py
│   └── test_arithmetic.py   # Unit tests
├── main.py                  # Entry script (placeholder)
├── pyproject.toml           # Package metadata and build config
├── uv.lock                  # Locked dependencies (uv)
├── LICENSE                  # MIT License
└── README.md
```

The project uses the **src layout**: importable code lives under `src/mathlib_evanjjh/`, which keeps the installed package separate from the project root during development.

## Development

### 1. Initialize the project (first-time setup)

This project was bootstrapped with uv:

```bash
uv init .
mkdir -p src/mathlib_evanjjh
touch src/mathlib_evanjjh/__init__.py
mkdir tests
touch tests/__init__.py
```

### 2. Install dev dependencies

```bash
uv sync --group dev
```

Dev dependencies (defined in `pyproject.toml`):

- `pytest>=8.0` — test runner
- `twine>=6.1.0` — PyPI upload tool

### 3. Run tests

```bash
uv run pytest tests/test_arithmetic.py -v
```

All five tests should pass:

- `test_add`
- `test_subtract`
- `test_multiply`
- `test_divide`
- `test_divide_by_zero`

## Publishing to PyPI

This section documents the workflow used to publish `mathlib-evanjjh` to PyPI.

### Prerequisites

1. Create a [PyPI account](https://pypi.org/account/register/).
2. Generate an **API token** at [https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/).
3. Bump the version in `pyproject.toml` before each new release. PyPI does not allow re-uploading the same file name; attempting to publish an existing version returns:

   ```
   400 File already exists ('mathlib_evanjjh-0.1.0-py3-none-any.whl', ...)
   ```

   In this project, version `0.1.0` was published first; `0.1.1` was published after bumping the version.

### Step 1 — Run tests

Always verify tests pass before building:

```bash
uv run pytest tests/test_arithmetic.py -v
```

### Step 2 — Build distribution files

```bash
uv build
```

This produces two files under `dist/`:

- `mathlib_evanjjh-<version>.tar.gz` (source distribution)
- `mathlib_evanjjh-<version>-py3-none-any.whl` (wheel)

Example output:

```
Successfully built dist/mathlib_evanjjh-0.1.1.tar.gz
Successfully built dist/mathlib_evanjjh-0.1.1-py3-none-any.whl
```

If you need a clean rebuild, remove the old artifacts first:

```bash
rm -rf dist/
uv build
```

### Step 3 — Configure PyPI credentials

Choose one of the following methods.

#### Option A: Environment variable (recommended for CI and local use)

Create a `.env` file in the project root (already listed in `.gitignore`):

```bash
UV_PUBLISH_TOKEN=pypi-<your-api-token>
```

Then publish with uv:

```bash
source .env
uv publish
```

When prompted, enter:

- **Username:** `__token__`
- **Password:** your API token (or rely on `UV_PUBLISH_TOKEN`)

#### Option B: `~/.pypirc` file

Create `~/.pypirc` in your home directory:

```ini
[pypi]
username = __token__
password = pypi-<your-api-token>
```

> Never commit API tokens to version control. Both `.env` and `.pypirc` are excluded via `.gitignore`.

### Step 4 — Upload to PyPI

#### Using uv (built-in publish)

```bash
uv publish
```

#### Using twine (alternative)

Install twine as a dev dependency (already included):

```bash
uv add --dev twine
```

Upload with:

```bash
uv run twine upload dist/*
```

> Use `uv run twine` rather than calling `twine` directly, since twine is installed in the project virtual environment.

On success, PyPI returns a link to the release page:

```
https://pypi.org/project/mathlib-evanjjh/<version>/
```

### Release checklist

1. Update `version` in `pyproject.toml`.
2. Run tests: `uv run pytest -v`
3. Build: `uv build`
4. Upload: `uv publish` or `uv run twine upload dist/*`
5. Verify on [https://pypi.org/project/mathlib-evanjjh/](https://pypi.org/project/mathlib-evanjjh/)
6. Install and smoke-test: `pip install mathlib-evanjjh==<version>`

## Roadmap

Planned additions (from the package description):

- Geometric sequence utilities
- Trigonometry helpers

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**EvanJJH** — [j2hoon85@gmail.com](mailto:j2hoon85@gmail.com)

- Homepage: [https://github.com/dschloe/mathlib-evanjjh](https://github.com/dschloe/mathlib-evanjjh)
