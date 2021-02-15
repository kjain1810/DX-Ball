from time import time

from .settings import *


class Player():
    """The main player class"""

    def __init__(self):
        self.paddleLength = INIT_PADDLE_LENGTH
        self.paddleLeft = int(BOARD_WIDTH / 2 - INIT_PADDLE_LENGTH)
        self.catchBalls = False
        self.lives = 3
        self.score = 0
        self.time = 0
        self.start_time = time()
        self.grabPaddle = False

    def movePaddleLeft(self, balls):
        """Moving the paddle to the left if it can"""
        if self.paddleLeft == 0:
            return
        if self.paddleLeft == 1:
            self.paddleLeft = 0
            for ball in balls:
                if ball.x == BOARD_HEIGHT - 1 and ball.velocity["x"] == 0:
                    ball.y -= 1
            return
        self.paddleLeft -= 2
        for ball in balls:
            if ball.x == BOARD_HEIGHT - 1 and ball.velocity["x"] == 0:
                ball.y -= 2

    def movePaddleRight(self, balls):
        """Moving the paddle to the right if it can"""
        if self.paddleLeft + self.paddleLength == BOARD_WIDTH:
            return
        if self.paddleLeft + self.paddleLength == BOARD_WIDTH - 1:
            self.paddleLeft += 1
            for ball in balls:
                if ball.x == BOARD_HEIGHT - 1 and ball.velocity["x"] == 0:
                    ball.y += 1
            return
        self.paddleLeft += 2
        for ball in balls:
            if ball.x == BOARD_HEIGHT - 1 and ball.velocity["x"] == 0:
                ball.y += 2

    def reduceLife(self):
        """When the player loses all the balls"""
        self.lives -= 1

    def setTime(self):
        """Set the playing time of the player"""
        self.time = int(time() - self.start_time)

    def increaseScore(self, points):
        """Update the score of the player"""
        self.score += points
