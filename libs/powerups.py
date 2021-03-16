from colorama import Back, Style, Fore

from .block import Block
from .settings import *
from .ball import Ball


class PowerUps(Block):
    """Parent class for the different powerups"""

    def __init__(self, x, y, vely, otp):
        Block.__init__(self, x, y, 1, vely, otp)

    def doPowerUp(self, player, balls):
        """Super function for all powerups"""
        pass

    def move(self, player, balls):
        """Moves the powerup a block down"""
        self.x += self.velocity["x"]
        self.y += self.velocity["y"]
        if self.y < 0:
            self.y = 0
            self.velocity["y"] = -self.velocity["y"]
        if self.y >= BOARD_WIDTH:
            self.y = BOARD_WIDTH - 1
            self.velocity["y"] = -self.velocity["y"]
        if self.x == BOARD_HEIGHT - 1:
            if self.y >= player.paddleLeft and self.y < player.paddleLeft + player.paddleLength:
                self.doPowerUp(player, balls)
            return False
        return True


class ExpandPaddle(PowerUps):
    """Power up to expand the player's paddle"""

    def __init__(self, x, y, vely):
        PowerUps.__init__(self, x, y, vely, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " E " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        """Expansd the paddle of the player"""
        player.increasePaddleSize()


class ShrinkPaddle(PowerUps):
    """Power up to shrink the player's paddle"""

    def __init__(self, x, y, vely):
        PowerUps.__init__(self, x, y, vely, Style.BRIGHT + Fore.BLACK +
                          Back.RED + " S " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        """Shrinks the paddle of the player"""
        player.decreasePaddleSize()


class BallMultiplier(PowerUps):
    def __init__(self, x, y, vely):
        PowerUps.__init__(self, x, y, vely, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " B " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        """Creates a copy of each ball with diagonal velocity"""
        newBalls = []
        for ball in balls:
            newBalls.append(
                Ball(ball.x, ball.y, ball.velocity["x"], -ball.velocity["y"], ball.thru_ball, True))
        for ball in newBalls:
            balls.append(ball)


class FastBall(PowerUps):
    """Power up to increase the speed of the ball"""

    def __init__(self, x, y, vely):
        PowerUps.__init__(self, x, y, vely, Style.BRIGHT + Fore.BLACK +
                          Back.RED + " F " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        """Increases speed of each ball"""
        player.increaseSpeed()


class ThruBall(PowerUps):
    """Power up to make the ball go through blocks"""

    def __init__(self, x, y, vely):
        PowerUps.__init__(self, x, y, vely, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " T " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        """Makes the ball a thru ball"""
        for ball in balls:
            ball.thru_ball = POWERUP_TIME


class PaddleGrab(PowerUps):
    """Power up to make the paddle grab the balls"""

    def __init__(self, x, y, vely):
        PowerUps.__init__(self, x, y, vely, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " G " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        """Makes the paddle grab stuff"""
        player.grabPaddle = POWERUP_TIME
