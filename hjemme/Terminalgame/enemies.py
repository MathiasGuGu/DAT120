from dataclasses import dataclass, field
from typing import Optional, List
from random import random

@dataclass(order=True, frozen=True)
class Wolf:
    sort_index: int = field(init=False, repr= False)
    boss: Optional[bool]
    type: str = "Wolf"
    lvl: int = 10
    strenght: int = 100 + (lvl * 15)
    health: int = 100 + (lvl * 50)

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.lvl)

    def __str__(self) -> str:
        return f"Type: {self.type}, it has {self.health} health, and {self.strenght} strenght"


    def attack():
        pass

    def defend():
        pass

