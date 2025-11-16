Habit Tracker – Python 3.7+

This project is a minimal habit tracking backend demonstrating object-oriented programming, functional programming, and SQLite persistence using only the Python standard library. It was developed for the IU module DLBDSOOFPP01 – Object Oriented and Functional Programming with Python.

The application includes an OOP core consisting of the Habit dataclass and the HabitRepo repository for data persistence. Functional analytics are provided through pure helper functions capable of listing habits, filtering by periodicity, computing the longest streak for a given habit, and determining the longest streak overall. The system uses a lightweight SQLite database with automatic schema creation and foreign key support, with local storage at data/habits.sqlite. A simple CLI interface allows users to list, filter, create, delete, check off habits, and view streaks. Unit tests are included and run against a temporary SQLite database to ensure isolation and reliability. The project uses no external dependencies and relies entirely on the Python standard library.

To run the application, open a terminal in the project root and execute: python -m habits.cli
The command launches the text-based menu. If the database is empty, the system automatically seeds five predefined habits, including daily and weekly periodicities, along with approximately four weeks of sample check-off data.

To run the test suite, use: python -m unittest
Tests automatically create a temporary SQLite database for each run, ensuring that the test environment does not interfere with production data and eliminating UNIQUE constraint conflicts. This setup guarantees deterministic, repeatable, and isolated test behaviour.

The project structure is organised as follows:
habits – models, storage logic, and CLI entry point
analytics – functional analytics helpers
tests – unit tests
data – database file and sample seed fixtures
docs – UML diagrams and project deliverables
README.md – project overview and usage instructions

The project requires Python version 3.7 or higher and uses only standard library modules, including dataclasses, sqlite3, unittest, datetime, and pathlib.

SQLite foreign key support is enabled using “PRAGMA foreign_keys = ON;”. The seed process executes only if the database has no existing habits, ensuring that example data is never duplicated or overwritten. Streak calculations correctly differentiate between daily and weekly rules and follow a deterministic logic based on recorded timestamps.
