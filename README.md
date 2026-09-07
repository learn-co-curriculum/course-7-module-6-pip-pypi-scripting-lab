# Module Lab: Automating Python Projects with Pip, PyPI & Scripting

## Project Description

This project is a Python automation tool that demonstrates the use of Python scripting, pip-installed packages, API requests, and file I/O.

The program:

- Validates input data.
- Creates a timestamped log file.
- Writes log entries to a text file.
- Prints a confirmation message.
- Fetches data from a public API using the `requests` package.
- Tracks dependencies using `requirements.txt`.
- Uses the `if __name__ == "__main__"` entry point.

## Learning Goals

- Automate Python tasks using command-line scripts.
- Use pip to install and manage external packages.
- Write modular Python scripts using functions.
- Track dependencies using `requirements.txt`.
- Generate files using Python File I/O.
- Fetch data from an external API.

## Project Structure

```text
course-7-module-6-pip-pypi-scripting-lab/
│
├── lib/
│   ├── __init__.py
│   └── generate_log.py
│
├── testing/
│   ├── __init__.py
│   └── test_generate_log.py
│
├── requirements.txt
├── Pipfile
├── Pipfile.lock
├── pytest.ini
├── README.md
├── CONTRIBUTING.md
└── LICENSE.md