import unittest
from pathlib import Path
from habits.storage import HabitRepo
from analytics.functions import list_by_periodicity

class TestBasics(unittest.TestCase):
    def setUp(self):
        # use a separate test DB so we don't touch the main one
        self.repo = HabitRepo(Path("data/test.sqlite"))

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
