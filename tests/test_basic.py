import tempfile
import unittest

from habits.storage import HabitRepo
from analytics.functions import list_by_periodicity


class TestBasics(unittest.TestCase):
    def setUp(self):
        # Create a unique temporary SQLite file for this test run
        tmp = tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False)
        self.db_path = tmp.name
        tmp.close()  # Close OS handle so sqlite can open it

        self.repo = HabitRepo(self.db_path)
        self.repo._init_db()  # Create habits and checkoffs tables

    def test_create_and_list(self):
        hid = self.repo.add_habit("TestDaily", "daily")
        self.assertTrue(hid > 0)
        habits = self.repo.list_habits()
        self.assertTrue(any(h.name == "TestDaily" for h in habits))

    def test_periodicity_filter(self):
        self.repo.add_habit("A", "daily")
        self.repo.add_habit("B", "weekly")
        dailies = list_by_periodicity(self.repo, "daily")
        self.assertTrue(any(h.name == "A" for h in dailies))
        self.assertFalse(any(h.name == "B" for h in dailies))


if __name__ == "__main__":
    unittest.main()
