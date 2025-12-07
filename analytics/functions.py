from datetime import datetime
from typing import List
from habits.models import Habit
from habits.storage import HabitRepo

def list_all_habits(repo: HabitRepo) -> List[Habit]:
"""Return all habits from the repository."""
    return repo.list_habits()

def list_by_periodicity(repo: HabitRepo, periodicity: str) -> List[Habit]:
"""Return habits filtered by periodicity (daily or weekly)."""
    return [h for h in repo.list_habits() if h.periodicity == periodicity]

def longest_streak_for_habit(repo: HabitRepo, habit: Habit) -> int:
"""Compute the longest on time streak for a single habit."""
    stamps = repo.get_checkoffs(habit.id)
    if not stamps:
        return 0
    if habit.periodicity == "daily":
        return _longest_consecutive_days(stamps)
    return _longest_consecutive_weeks(stamps)

def longest_streak_overall(repo: HabitRepo) -> int:
"""Return the best streak across all habits in the repository."""
    return max((longest_streak_for_habit(repo, h) for h in repo.list_habits()), default=0)

def _longest_consecutive_days(stamps: List[datetime]) -> int:
    days = sorted({dt.date() for dt in stamps})
    best = cur = 1
    for prev, nxt in zip(days, days[1:]):
        if (nxt - prev).days == 1:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best

def _longest_consecutive_weeks(stamps: List[datetime]) -> int:
    weeks = sorted({(dt.isocalendar()[0], dt.isocalendar()[1]) for dt in stamps})
    best = cur = 1
    for (y1, w1), (y2, w2) in zip(weeks, weeks[1:]):
        next_week = (y1, w1 + 1)
        if w1 == 52 and w2 == 1 and y2 == y1 + 1:
            next_week = (y2, 1)
        if (y2, w2) == next_week:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best
