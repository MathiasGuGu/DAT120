from dataclasses import dataclass, field
from typing import Optional, List
from random import random

class GenerateRandomNumber:
    def Random() -> int:
        n = round(random()*5)
        return n
