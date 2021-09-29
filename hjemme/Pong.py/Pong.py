from dataclasses import dataclass
import time
import turtle as t

""" Make a function so the player can move."""
@dataclass
class Player:
    lives: int
    speed: int
    position_x: int = - 600
    position_y: int = 0


    def draw_player(position_x, position_y):
        """ Funciton that draws player as a line on the left side of the screen"""
        t.pu()
        t.goto(position_x, position_y)
        t.left(90)
        t.pd()
        t.forward(100)
        t.pu()
        t.done()


    def move(self):
        pass

    def calculate_lives(lives):
        """ Calculate the lives of both the player and the enemy """



""" Make a function so the player can move."""
@dataclass
class Enemy:
    lives: int
    speed: int
    position_x: int = 600
    position_y: int = 0


    def draw_enemy(position_x, position_y):
        """ Funciton that draws enemy as a line on the right side of the screen"""
        t.pu()
        t.goto(-position_x, position_y)
        t.left(90)
        t.pd()
        t.forward(100)
        t.pu()
        t.done()


    def move():
        pass

    def calculate_lives(lives):
        """ Calculate the lives of both the player and the enemy """


class Board:
    def __init__(self, width: int, mode: str) -> None:
        self.width = width
        self.mode = mode
    
    def create_board(self):
        """ Use turle to create a window """
        t.speed(5)
        t.screensize(self.width, self.width * 0.8)
        t.color = "black"
        
        Enemy.draw_enemy(Enemy.position_x, Enemy.position_y)
        Player.draw_player(Player.position_x, Player.position_y)
    

""" Use this to see if game is won, calculate movement ... """
class loop:
    def game_logic():
        board = Board(1080, "Single")
        board.create_board()
            
    


class Game:
    """ Define a game loop """
    def run():
        while True:
        # dt is the time delta in seconds (float).
            currentTime = time.time()
            lastFrameTime = currentTime

            dt = currentTime - lastFrameTime

            loop.game_logic()

if __name__ == "__main__":
    Game.run()
