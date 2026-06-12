# Task Automation CLI Tool

## Overview

This project is a lightweight Python automation tool built using Object-Oriented Programming (OOP), CLI architecture, and external packages. It allows users to create and manage simple tasks and generate log files from structured data. It is designed to demonstrate real-world Python scripting, dependency management, and reproducible environments using `pip` and `requirements.txt`.

---

## Features

* Add tasks via command line (`add-task`)
* Mark tasks as complete (`complete-task`)
* List all tasks in terminal (`list-tasks`)
* Generate log files from structured data
* Fetch sample data from external API using `requests`
* Save structured data using File I/O (CSV + TXT files)
* Fully testable using `pytest`

---

## Project Structure

```
project/
│
├── lib/
│   ├── generate_log.py
│   ├── task.py
│   └── task_manager.py
│
├── cli.py
├── testing/
│   └── test_generate_log.py
│
├── requirements.txt
├── tasks.csv
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:wanja-juma/course-7-module-6-pip-pypi-scripting-lab.git
cd <project-folder>
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Add a task

```bash
python cli.py add-task "Finish Python project"
```

### Add task from API

```bash
python cli.py add-task
```

### List tasks

```bash
python cli.py list-tasks
```

### Complete a task

```bash
python cli.py complete-task 1
```

---

## Running Tests

Make sure pytest is installed:

```bash
pip install pytest
```

Run tests:

```bash
pytest
```

---

## Generate Logs

You can manually run the logging script:

```bash
python lib/generate_log.py
```

Or use it as a function inside your code:

```python
from lib.generate_log import generate_log

generate_log(["Event 1", "Event 2"])
```

---

## Dependencies

All dependencies are tracked in `requirements.txt`:

```
requests
pandas
pytest
```

Freeze environment:

```bash
pip freeze > requirements.txt
```

---

## Technologies Used

* Python 3
* OOP (Object-Oriented Programming)
* argparse (CLI handling)
* requests (API calls)
* pytest (testing)
* File I/O (CSV + TXT handling)

---

## Author

Built as a Python CLI automation lab project focusing on scripting, pip, and reproducible environments.
