from dataclasses import dataclass, field
from typing import Optional, List
from random import random

@dataclass(order=True, frozen=True)
class Player:
    sort_index: int = field(init=False, repr = False)
    name: str
    surname: str
    height: Optional[int]
    lvl: int = 1
    strength: int = 100
    health: int = 100

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.strength)

    def __str__(self) -> str:
        return f"Name: {self.name} {self.surname}, Strenght: {self.strength}, Health: {self.health}"


    # class defined methods
    def compute_health(self) -> int:
        return (
            self.health + (self.lvl * 25)
        )

    def compute_attack(self) -> int:
        return (
            self.strength + (self.lvl * 10)
        )

    def attack():
        pass
        
    def defend():
        pass

