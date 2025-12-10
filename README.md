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

run:
  
  - python -m habits.cli

## CLI

The CLI allows you to:

- list habits

- filter by daily or weekly periodicity

- create habits

- delete habits

- check off habits

- view longest streaks

If the database is empty, the application seeds:

- five predefined habits

- four weeks of sample check offs

## Running Tests
Run all tests with:

  python -m unittest

Each test run uses a temporary SQLite database to ensure:

- isolation from the main database

- no UNIQUE constraint conflicts

- deterministic and repeatable results

## Project Structure
- analytics/ <----> Functional analytics (filters, streak calculations)
- data/ <----> SQLite database and seed data
- habits/ <----> Core logic (models, storage, CLI)
- tests/ <----> Unit tests
- README.md <----> This file
- .gitignore <----> Ignore unnecessary files

## Technical Requirements
- Requires Python 3.7 or higher.
- Runs on any OS where Python is avaiable.

## How it works and internals:

- habits.models defines the Habit dataclass

- habits.storage implements HabitRepo, encapsulating SQLite operations: schema creation, CRUD, check-offs

- analytics.functions provides pure-function analytics for filtering habits and computing streaks

- habits.cli implements the CLI entry point (python -m habits.cli), including seeding logic on first run

- Unit tests in tests/ verify core functionality and analytics logic using temporary databases


Uses only standard library modules:

- dataclasses

- sqlite3

- datetime

- unittest

- pathlib

- tempfile

## Notes
SQLite foreign keys are enabled using PRAGMA foreign_keys = ON

Seed data is inserted only if the database is empty

Streak rules differentiate correctly between daily and weekly habits

## Screenshots

CLI in action:

<img width="860" height="806" alt="image" src="https://github.com/user-attachments/assets/2b2c05d7-f7e5-4116-b1c9-416778c3d63e" />


Unit tests:

<img width="1089" height="215" alt="Tests_Pass" src="https://github.com/user-attachments/assets/b0c3c427-cb9a-4884-adf6-f2b0c1496f0e" />

## Summary

This project demonstrates how object-oriented programming (for state and persistence) and functional programming (for analytics) can coexist cleanly in a small Python application.
It provides a simple but fully functional habit-tracking backend which is perfect as a learning example or small personal tool.

Enjoy tracking your habits!
