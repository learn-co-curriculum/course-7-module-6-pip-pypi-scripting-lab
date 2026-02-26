# Course 7 Module 6: Pip, PyPI & Scripting Lab

## Overview

This lab demonstrates how to:

- Use pipenv to manage dependencies
- Structure a Python project using modules
- Write testable Python functions
- Use pytest for automated testing
- Follow proper Git branching workflow

## Project Structure

```
lib/
    generate_log.py
testing/
    test_generate_log.py
Pipfile
Pipfile.lock
pytest.ini
```

## Functionality

The `generate_log` function:

- Accepts a list of log entries
- Validates that input is a list
- Generates a filename using today's date
- Writes each log entry to a file
- Returns the generated filename

Example output file:

```
log_20260226.txt
```

## Input Validation

- Raises `ValueError` if input is not a list
- Creates an empty file if an empty list is provided

## Running Tests

Activate pipenv environment:

```bash
pipenv shell
```

Run tests:

```bash
pipenv run pytest
```

All tests should pass.

## Git Workflow Used

- Created feature branch: `feature-automation-tool`
- Implemented functionality
- Committed changes
- Opened pull request
- Merged into main

## Key Concepts Practiced

- Virtual environments with pipenv
- Dependency tracking via Pipfile
- File I/O operations
- Automated testing with pytest
- Professional Git workflow