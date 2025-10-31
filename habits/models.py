from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Literal

Periodicity = Literal["daily", "weekly"]

@dataclass(frozen=True)
class Habit:
    id: Optional[int]
    name: str
    periodicity: Periodicity
    created_at: datetime
