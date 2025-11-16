# Habit Tracker (Python 3.7+)

A minimal habit tracking backend demonstrating Object Oriented Programming, Functional Programming, and SQLite persistence using only the Python standard library. Developed for the IU module DLBDSOOFPP01.

---

## Features

- OOP core: Habit dataclass and HabitRepo repository  
- Functional analytics: pure functions for periodicity filtering and streak computation  
- SQLite persistence with automatic schema creation  
- CLI interface using standard input and output  
- Unit tests using isolated temporary databases  
- No external dependencies  

---

## Quick Start

From the project root directory:

```bash
python -m habits.cli
The CLI allows you to:

list habits

filter by daily or weekly

create habits

delete habits

check off habits

view longest streaks

If the database is empty, the application seeds:

five predefined habits

four weeks of sample check offs

Running Tests
Run all tests with:

bash
Copy code
python -m unittest
Each test run uses a temporary SQLite database to ensure:

isolation from the main database

no UNIQUE constraint conflicts

deterministic and repeatable results

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
SQLite foreign keys are enabled with PRAGMA foreign_keys = ON

Seed data is inserted only if the database is empty

Streak rules differentiate correctly between daily and weekly habits
