from time import time

from .settings import *
from .bricks import RainbowBrick
from .bullets import Bullet


class Player():
    """The main player class"""

    def __init__(self):
        self.paddleLength = INIT_PADDLE_LENGTH
        self.paddleLeft = int(BOARD_WIDTH / 2 - INIT_PADDLE_LENGTH)
        self.catchBalls = False
        self.lives = 3
        self.score = 0
        self.time = 0
        self.levelTime = 0
        self.level_start_time = time()
        self.lUpdateRainbow = 0
        self.lUpdateFall = 0
        self.fallingBricks = False
        self.start_time = time()
        self.grabPaddle = 0
        self.changePaddleSize = []
        self.speed = 1
        self.changeSpeed = []
        self.level = 0
        self.shootingPaddle = 0
        self.lBullet = 0

    def resetLevel(self):
        self.paddleLength = INIT_PADDLE_LENGTH
        self.paddleLeft = int(BOARD_WIDTH / 2 - INIT_PADDLE_LENGTH)
        self.catchBalls = False
        self.grabPaddle = 0
        self.changePaddleSize = []
        self.speed = 1
        self.changeSpeed = []
        self.level_start_time = time()
        self.levelTime = 0
        self.fallingBricks = False
        self.shootingPaddle = 0

    def makeShot(self, bullets):
        if self.time - self.lBullet < BULLET_TIME:
            return
        self.lBullet = self.time
        bullets.append(Bullet(BOARD_HEIGHT - 1, self.paddleLeft))
        bullets.append(
            Bullet(BOARD_HEIGHT - 1, self.paddleLeft + self.paddleLength - 1))

    def setPaddleOutput(self, ret):
        if self.shootingPaddle == 0:
            for i in range(self.paddleLeft, self.paddleLeft + self.paddleLength):
                ret[BOARD_HEIGHT - 1][i] = PADDLE_OUTPUT
        else:
            for i in range(self.paddleLeft + 1, self.paddleLeft + self.paddleLength - 1):
                ret[BOARD_HEIGHT - 1][i] = PADDLE_OUTPUT
            ret[BOARD_HEIGHT - 1][self.paddleLeft] = PADDLE_SHOOTER_OUTPUT
            ret[BOARD_HEIGHT - 1][self.paddleLeft +
                                  self.paddleLength - 1] = PADDLE_SHOOTER_OUTPUT
        return ret

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

    def setTime(self, bricks):
        """Set the playing time of the player"""
        self.time = int(time() - self.start_time)
        self.levelTime = int(time() - self.level_start_time)
        if self.time - self.lUpdateRainbow >= RAINBOW_TIME:
            self.lUpdateRainbow = self.time
            for brick in bricks:
                if type(brick) == RainbowBrick:
                    brick.changeCol()
        if self.levelTime >= FALL_TIME:
            self.fallingBricks = True

    def increaseScore(self, points):
        """Update the score of the player"""
        self.score += points

    def checkPowerUps(self):
        if self.grabPaddle > 0:
            self.grabPaddle -= 1
        if self.shootingPaddle > 0:
            self.shootingPaddle -= 1
        to_rem = []
        for upd in self.changePaddleSize:
            upd["time"] -= 1
            if upd["time"] == 0:
                if upd["action"] == "increase":
                    self.increasePaddleSize(powerup=False)
                elif upd["action"] == "decrease":
                    self.decreasePaddleSize(powerup=False)
                to_rem.append(upd)
        self.changePaddleSize = [
            upd for upd in self.changePaddleSize if upd not in to_rem]

        to_rem = []
        for upd in self.changeSpeed:
            upd["time"] -= 1
            if upd["time"] == 0:
                if upd["action"] == "increase":
                    self.increaseSpeed(powerup=False)
                elif upd["action"] == "decrease":
                    self.decreaseSpeed(powerup=False)
                to_rem.append(upd)
        self.changeSpeed = [
            upd for upd in self.changeSpeed if upd not in to_rem]

    def increasePaddleSize(self, powerup=True):
        self.paddleLength += 2
        self.paddleLeft -= 1
        if self.paddleLength > MAX_PADDLE_LENGTH:
            self.paddleLength = MAX_PADDLE_LENGTH
        if self.paddleLeft < 0:
            self.paddleLeft = 0
        if self.paddleLeft + self.paddleLength - 1 >= BOARD_WIDTH:
            self.paddleLeft = BOARD_WIDTH - self.paddleLength
        if powerup:
            self.changePaddleSize.append(
                {"action": "decrease", "time": POWERUP_TIME})

    def decreasePaddleSize(self, powerup=True):
        self.paddleLength -= 2
        if self.paddleLength < MIN_PADDLE_LENGTH:
            self.paddleLength = MIN_PADDLE_LENGTH
        else:
            self.paddleLeft += 1
        if powerup:
            self.changePaddleSize.append(
                {"action": "increase", "time": POWERUP_TIME})

    def increaseSpeed(self, powerup=True):
        self.speed += 1
        if powerup:
            self.changeSpeed.append(
                {"action": "decrease", "time": POWERUP_TIME})

    def decreaseSpeed(self, powerup=True):
        self.speed -= 1
        if powerup:
            self.changeSpeed.append(
                {"action": "increase", "time": POWERUP_TIME})
