# Habit Tracker (Python 3.7+)

A minimal habit tracking backend demonstrating Object Oriented Programming, Functional Programming, and SQLite persistence using only the Python standard library. Developed for the IU module DLBDSOOFPP01 (Object Oriented and Functional Programming with Python).

---

## Features

- OOP core: Habit dataclass and HabitRepo repository for persistence  
- Functional analytics: pure functions for listing habits, filtering by periodicity, and calculating longest streaks  
- SQLite persistence: automatic schema creation, foreign key enforcement, and storage in data/habits.sqlite  
- CLI interface: simple text based menu  
- Unit tests: each test uses an isolated temporary SQLite database  
- No external dependencies: Python standard library only  

---

## Quick Start

From the project root directory:

```bash
python -m habits.cli
The CLI menu allows you to:

list habits

filter by daily or weekly periodicity

create new habits

delete habits

check off habits

view longest streaks

If the database is empty, the application seeds:

five predefined habits (daily and weekly)

approximately four weeks of sample check offs

Running Tests
Run all tests with:

bash
Copy code
python -m unittest
The test suite uses a temporary SQLite database for each test run. This ensures:

full isolation from the main application database

no UNIQUE constraint conflicts

deterministic and repeatable test results

Project Structure
kotlin
Copy code
habits/         models, storage logic, CLI entry point  
analytics/      functional analytics helpers  
tests/          unit tests  
data/           database file and seed fixtures  
docs/           UML diagrams and Phase deliverables  
README.md       this file  
Python Version
Requires Python 3.7 or higher.

Uses only standard library modules:

dataclasses

sqlite3

datetime

unittest

pathlib

tempfile

Notes
SQLite foreign keys are enforced with:
PRAGMA foreign_keys = ON

The seed function runs only when the database is empty and does not overwrite user data

Streak calculations correctly follow daily versus weekly rules
