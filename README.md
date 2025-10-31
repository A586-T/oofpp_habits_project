# Habit Tracker (DLBDSOOFPP01)

A minimal habit tracking backend in Python 3.7+:
- OOP core (`Habit`, `HabitManager`)
- Functional analytics (pure functions in `analytics/`)
- SQLite persistence (standard library `sqlite3`)
- CLI interface (no 3rd-party deps)
- Unit tests

## Quick start
python -m habits.cli

## Project layout
- `habits/` – models, storage, CLI
- `analytics/` – functional analysis helpers
- `tests/` – unit tests (unittest)
- `data/` – seeded DB and fixtures
- `docs/` – UML and phase deliverables (PDFs)

## Python
- 3.7+ (uses `dataclasses` and stdlib only)

## Notes
- Five predefined habits (daily & weekly) and 4 weeks of sample check-offs are seeded on first run.
