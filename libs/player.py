from .settings import *


class Player():
    def __init__(self):
        self.paddleLength = 5
        self.paddleLeft = int(BOARD_WIDTH / 2 - 5)
        self.catchBalls = False
        self.lives = 3
        self.score = 0
        self.time = 0
        self.speed = 1

    def movePaddleLeft(self, balls):
        if(self.paddleLeft == 0):
            return
        self.paddleLeft -= 1
        for ball in balls:
            if ball.x == BOARD_HEIGHT - 1 and ball.velocity["x"] == 0:
                ball.y -= 1

    def movePaddleRight(self, balls):
        if(self.paddleLeft + self.paddleLength == BOARD_WIDTH):
            return
        self.paddleLeft += 1
        for ball in balls:
            if ball.x == BOARD_HEIGHT - 1 and ball.velocity["x"] == 0:
                ball.y += 1

    def reduceLife(self):
        self.lives -= 1
