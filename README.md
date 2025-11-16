# Habit Tracker (Python 3.7+)

A minimal habit tracking backend demonstrating Object Oriented Programming, Functional Programming, and SQLite persistence using only the Python standard library. Developed for the IU module DLBDSOOFPP01 – Object Oriented and Functional Programming with Python.

## Features

- OOP core: Habit dataclass and HabitRepo repository for persistence.
- Functional analytics: pure functions for listing habits, filtering by periodicity, and calculating longest streaks.
- SQLite persistence: automatic schema creation, foreign key enforcement, and local storage in data/habits.sqlite.
- CLI interface: simple text based menu for interaction.
- Unit tests: isolated test database created automatically for each test run.
- No external dependencies: uses only the Python standard library.

## Quick Start

From the project root directory:

```bash
python -m habits.cli

## The CLI menu allows you to:

list habits

filter by daily or weekly periodicity

create or delete habits

check off a habit

view longest streaks

If the database is empty, the application seeds:

five predefined habits (daily and weekly)

approximately four weeks of sample check offs

Running Tests
Run all unittests with:

bash
Copy code
python -m unittest
Tests use a temporary SQLite database for full isolation. This ensures that:

tests never interfere with the main application database

the UNIQUE constraint on habit names never causes conflicts

all tests are deterministic and repeatable

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
Uses only the following standard library modules:

dataclasses

sqlite3

datetime

unittest

pathlib

tempfile

Notes
Foreign keys are enforced using:
PRAGMA foreign_keys = ON;

The seed function runs only when the database is empty and does not overwrite user data.

Streak calculations correctly follow daily versus weekly rules.
