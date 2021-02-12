from .settings import *
from time import time


class Player():
    """The main player class"""

    def __init__(self):
        self.paddleLength = 5
        self.paddleLeft = int(BOARD_WIDTH / 2 - 5)
        self.catchBalls = False
        self.lives = 3
        self.score = 0
        self.time = 0
        self.speed = 1
        self.start_time = time()

    def movePaddleLeft(self, balls):
        """Moving the paddle to the left if it can"""
        if(self.paddleLeft == 0):
            return
        self.paddleLeft -= 1
        for ball in balls:
            if ball.x == BOARD_HEIGHT - 1 and ball.velocity["x"] == 0:
                ball.y -= 1

    def movePaddleRight(self, balls):
        """Moving the paddle to the right if it can"""
        if(self.paddleLeft + self.paddleLength == BOARD_WIDTH):
            return
        self.paddleLeft += 1
        for ball in balls:
            if ball.x == BOARD_HEIGHT - 1 and ball.velocity["x"] == 0:
                ball.y += 1

    def reduceLife(self):
        """When the player loses all the balls"""
        self.lives -= 1

    def setTime(self):
        """Set the playing time of the player"""
        self.time = int(time() - self.start_time)

    def increaseScore(self):
        """Update the score of the player"""
        self.score += 1
