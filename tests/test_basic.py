import tempfile
import unittest
from datetime import datetime, timedelta

from habits.storage import HabitRepo
from analytics.functions import (
    list_by_periodicity,
    longest_streak_for_habit,
    longest_streak_overall,
)


class TestBasics(unittest.TestCase):
    def setUp(self):
        # Each test uses its own temporary SQLite database file
        tmp = tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False)
        self.db_path = tmp.name
        tmp.close()

        self.repo = HabitRepo(self.db_path)
        self.repo._init_db()

    def test_create_and_list(self):
        """Creating a habit makes it appear in the list."""
        hid = self.repo.add_habit("TestDaily", "daily")
        self.assertTrue(hid > 0)
        habits = self.repo.list_habits()
        self.assertTrue(any(h.name == "TestDaily" for h in habits))

    def test_periodicity_filter(self):
        """Filtering by periodicity returns only matching habits."""
        self.repo.add_habit("A", "daily")
        self.repo.add_habit("B", "weekly")
        dailies = list_by_periodicity(self.repo, "daily")
        self.assertTrue(any(h.name == "A" for h in dailies))
        self.assertFalse(any(h.name == "B" for h in dailies))

    def test_delete_habit(self):
        """Deleting a habit removes it from the list."""
        hid = self.repo.add_habit("ToDelete", "daily")
        habits_before = self.repo.list_habits()
        self.assertTrue(any(h.name == "ToDelete" for h in habits_before))

        self.repo.delete_habit(hid)
        habits_after = self.repo.list_habits()
        self.assertFalse(any(h.name == "ToDelete" for h in habits_after))

    def test_longest_streak_for_daily_habit(self):
        """Daily habit with 28 consecutive days should have a streak of 28."""
        base = datetime(2024, 1, 1)
        hid = self.repo.add_habit("DailyStreak", "daily", created_at=base)

        # 28 consecutive daily checkoffs (4 weeks)
        for i in range(28):
            self.repo.check_off(hid, when=base + timedelta(days=i))

        habit = self.repo.get_habit_by_name("DailyStreak")
        streak = longest_streak_for_habit(self.repo, habit)
        self.assertEqual(streak, 28)

    def test_longest_streak_for_weekly_habit(self):
        """Weekly habit checked once per week over 4 weeks should have streak 4."""
        base = datetime(2024, 1, 1)
        hid = self.repo.add_habit("WeeklyStreak", "weekly", created_at=base)

        # 4 weekly checkoffs (once every 7 days)
        for i in range(4):
            self.repo.check_off(hid, when=base + timedelta(days=7 * i))

        habit = self.repo.get_habit_by_name("WeeklyStreak")
        streak = longest_streak_for_habit(self.repo, habit)
        self.assertEqual(streak, 4)

    def test_longest_streak_overall(self):
        """Overall streak should reflect the best habit."""
        base = datetime(2024, 1, 1)

        # Habit A: 3 day streak
        ha = self.repo.add_habit("A_streak", "daily", created_at=base)
        for i in range(3):
            self.repo.check_off(ha, when=base + timedelta(days=i))

        # Habit B: 5 day streak
        hb = self.repo.add_habit("B_streak", "daily", created_at=base)
        for i in range(5):
            self.repo.check_off(hb, when=base + timedelta(days=i))

        overall = longest_streak_overall(self.repo)
        self.assertEqual(overall, 5)


if __name__ == "__main__":
    unittest.main()
