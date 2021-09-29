from encounter import Encounter
from GenerateRandom import GenerateRandomNumber

class Move:

    true = False
    def forward():
        Move.true = True
        Encounter.enemy()
    def backward():
        Move.true = True
        Encounter.enemy()
    def left() -> None:
        Move.true = True
        Encounter.enemy()  
    def right():
        Move.true = True
        Encounter.enemy()