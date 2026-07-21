# Project Management CLI

A command-line Project Management System built with Python that demonstrates Object-Oriented Programming (OOP), JSON data persistence, command-line interfaces using `argparse`, and formatted terminal output using the `rich` library.

---

## Overview

This application allows an administrator to manage:

- Users
- Projects
- Tasks

Each user can own multiple projects, and each project can contain multiple tasks. Data is stored locally using JSON files, making the application lightweight and easy to run without a database.

---

## Features

### User Management

- Add a new user
- View all users
- Update user information

### Project Management

- Add a new project
- Assign a project to a user
- View all projects
- Update project details

### Task Management

- Add tasks to a project
- Assign tasks to users
- View all tasks
- Mark tasks as completed
- Update task information

### Data Persistence

- Save data using JSON
- Load existing data automatically when the application starts

### Object-Oriented Programming

The project demonstrates:

- Classes and Objects
- Inheritance
- Encapsulation
- Properties and Setters
- One-to-Many Relationships
- Instance Methods
- Class Methods
- Special Methods (`__str__`, `__repr__`)

### Additional Features

- Rich CLI tables using the `rich` package
- Unit testing using Python's `unittest`
- Git feature branch workflow

---

# Project Structure

```
project_cli/
│
├── models/
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── utils/
│   ├── storage.py
│   └── helpers.py
│
├── data/
│   ├── users.json
│   ├── projects.json
│   └── tasks.json
│
├── tests/
│   ├── test_user.py
│   ├── test_project.py
│   ├── test_task.py
│   ├── test_storage.py
│   └── test_cli.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Technologies Used

- Python 3
- argparse
- JSON
- Rich
- unittest
- Git
- GitHub

---

# Installation

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Change into the project directory.

```bash
cd YOUR_REPOSITORY
```

---

## Create a Virtual Environment

Linux / macOS

```bash
python3 -m venv venv
```

Windows

```bash
python -m venv venv
```

---

## Activate the Virtual Environment

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

## Add a User

```bash
python main.py add-user \
--name "Brian Kiprotich" \
--email "brian@gmail.com"
```

---

## View Users

```bash
python main.py list-users
```

---

## Update a User

```bash
python main.py update-user \
--user-id 1 \
--name "Brian K."
```

---

## Add a Project

```bash
python main.py add-project \
--title "GIS Mapping" \
--description "LV Network Survey" \
--due-date "2026-08-01" \
--user-id 1
```

---

## View Projects

```bash
python main.py list-projects
```

---

## Update a Project

```bash
python main.py update-project \
--project-id 1 \
--title "Updated GIS Mapping"
```

---

## Add a Task

```bash
python main.py add-task \
--title "Survey Pole Locations" \
--project-id 1 \
--assigned-to 1
```

---

## View Tasks

```bash
python main.py list-tasks
```

---

## Complete a Task

```bash
python main.py complete-task \
--task-id 1
```

---

## Update a Task

```bash
python main.py update-task \
--task-id 1 \
--status Completed
```

---

# Running Tests

Run all tests

```bash
python -m unittest discover tests
```

Run a specific test

```bash
python -m unittest tests.test_user
```

---

# Data Storage

The application stores information inside the `data` directory.

- users.json
- projects.json
- tasks.json

These files are automatically updated whenever changes are made through the CLI.

---

# Object Relationships

```
User
│
├── Project 1
│      ├── Task 1
│      ├── Task 2
│      └── Task 3
│
├── Project 2
│      ├── Task 4
│      └── Task 5
│
└── Project 3
```

---

# Known Limitations

- Uses JSON instead of a relational database.
- No authentication or authorization.
- No delete commands for users, projects, or tasks.
- IDs are generated locally and are not globally unique across distributed systems.

---

# Future Improvements

- SQLite or PostgreSQL integration
- User authentication
- Search and filtering commands
- Task priority levels
- Task due dates
- Export reports to CSV or PDF
- Interactive CLI using Typer or Click

---

# Author

**Brian Kiprotich**

Python CLI Project Management System

---

# License

This project is for educational purposes.