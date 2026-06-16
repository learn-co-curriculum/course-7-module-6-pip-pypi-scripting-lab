
# Module Lab: Automating Python Projects with Pip, PyPi & Scripting

# Automating Python Projects with Pip, PyPi & Scripting

## Overview

This project demonstrates how to build a simple automation tool using Python scripting, external packages, file handling, and command-line execution.

The project generates timestamped log files, stores log entries, and follows Python best practices for reproducible environments.

---

## Features

- Generate log files with today's date
- Write log entries to a text file
- Validate user input
- Raise exceptions for invalid data
- Execute from the command line
- Track dependencies using `requirements.txt`
- Automated testing with `pytest`

---

## Project Structure

```text
.
├── lib/
│   ├── __init__.py
│   └── generate_log.py
│
├── testing/
│   ├── __init__.py
│   └── test_generate_log.py
│
├── cli.py
├── README.md
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd course-7-module-6-pip-pypi-scripting-lab
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the CLI tool:

```bash
python cli.py add-task
```

or

```bash
python cli.py complete-task
```

---

## Example Output

Generated file:

```text
log_20260616.txt
```

Contents:

```text
Task created
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Expected output:

```text
5 passed
```

---

## Dependencies

Generate requirements file:

```bash
pip freeze > requirements.txt
```

---

## Learning Objectives

This project demonstrates:

- Python File I/O
- Functions and Validation
- Exception Handling
- Command-Line Interfaces (CLI)
- Dependency Management with Pip
- Automated Testing with Pytest
- Project Documentation

---

Built as part of the Moringa School Software Engineering Program.