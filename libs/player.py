from .settings import *

class Player():
    def __init__(self):
        self.balls = 1
        self.boardLength = 4
        self.catchBalls = False
        self.boardLeft = int(BOARD_WIDTH / 2 - 5)
        self.lives = 3
        self.score = 0
        self.time = 0