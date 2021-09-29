from dataclasses import dataclass, field
from typing import Optional, List
from random import random
from moves import Move

class World:
    def gameLoop():
        while True:
            move = input("Would you like to move? y/n ").lower()
            if (move != "y"):
                break
            elif move == "y":
                while True:
                    direction = input("in which direction? forward/backward/left/right ").lower()
                    if not (direction == "left".lower() or direction == "right".lower() or direction == "forward".lower() or direction == "backward".lower() or direction == ""):
                        print("Please write valid direction!")
                        continue
                    elif direction == "":
                        print("Please write a direction!")
                    elif direction == "forward".lower():
                        Move.forward()
                        if Move.true == False:
                            continue
                    elif direction == "backward".lower():
                        Move.backward()
                        if Move.true == False:
                            continue
                    elif direction == "left".lower():
                        Move.left()
                        if Move.true == False:
                            continue
                    elif direction == "right".lower():
                        Move.right()
                        if Move.true == False:
                            continue
            return

class initiate: 
    World.gameLoop()

if __name__ == "__main__":
    initiate
