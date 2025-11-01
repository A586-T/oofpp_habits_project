import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional
from .models import Habit

DB_PATH = Path("data/habits.sqlite")

SCHEMA = """
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS habits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  periodicity TEXT NOT NULL CHECK (periodicity IN ('daily','weekly')),
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS checkoffs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  habit_id INTEGER NOT NULL REFERENCES habits(id) ON DELETE CASCADE,
  done_at TEXT NOT NULL
);
"""

class HabitRepo:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self):
        con = sqlite3.connect(str(self.db_path))
        con.execute("PRAGMA foreign_keys=ON;")
        return con

    def _init_db(self):
        with self._connect() as con:
            con.executescript(SCHEMA)

    #Habits
    def add_habit(self, name: str, periodicity: str, created_at: Optional[datetime] = None) -> int:
        created_at = created_at or datetime.utcnow()
        with self._connect() as con:
            cur = con.execute(
                "INSERT INTO habits (name, periodicity, created_at) VALUES (?, ?, ?)",
                (name, periodicity, created_at.isoformat()),
            )
            return cur.lastrowid

    def delete_habit(self, habit_id: int):
        with self._connect() as con:
            con.execute("DELETE FROM habits WHERE id = ?", (habit_id,))

    def list_habits(self) -> List[Habit]:
        with self._connect() as con:
            rows = con.execute(
                "SELECT id, name, periodicity, created_at FROM habits ORDER BY name"
            ).fetchall()
        return [
            Habit(id=r[0], name=r[1], periodicity=r[2], created_at=datetime.fromisoformat(r[3]))
            for r in rows
        ]

    def get_habit_by_name(self, name: str) -> Optional[Habit]:
        with self._connect() as con:
            row = con.execute(
                "SELECT id, name, periodicity, created_at FROM habits WHERE name = ?",
                (name,),
            ).fetchone()
        if not row:
            return None
        return Habit(id=row[0], name=row[1], periodicity=row[2], created_at=datetime.fromisoformat(row[3]))

    #Check-offs
    def check_off(self, habit_id: int, when: Optional[datetime] = None):
        when = when or datetime.utcnow()
        with self._connect() as con:
            con.execute(
                "INSERT INTO checkoffs (habit_id, done_at) VALUES (?, ?)",
                (habit_id, when.isoformat()),
            )

    def get_checkoffs(self, habit_id: int) -> List[datetime]:
        with self._connect() as con:
            rows = con.execute(
                "SELECT done_at FROM checkoffs WHERE habit_id = ? ORDER BY done_at",
                (habit_id,),
            ).fetchall()
        return [datetime.fromisoformat(r[0]) for r in rows]

    def seed_if_empty(self):
        """Seed 5 habits (>=1 daily and >=1 weekly) and 4 weeks of sample data if DB is empty."""
        if self.list_habits():
            return
        habits = [
            ("Drink water", "daily"),
            ("Read 20 min", "daily"),
            ("Exercise", "daily"),
            ("Weekly review", "weekly"),
            ("Call family", "weekly"),
        ]
        ids = [self.add_habit(name, p) for name, p in habits]

        now = datetime.utcnow().replace(microsecond=0)
        for hid, (_, p) in zip(ids, habits):
            if p == "daily":
                for d in range(28):  #4 weeks
                    if (d % 13) != 0:  #miss a day sometimes
                        self.check_off(hid, when=now - timedelta(days=(27 - d)))
            else:
                for w in range(4):
                    self.check_off(hid, when=now - timedelta(days=7 * (3 - w)))
