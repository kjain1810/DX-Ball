from colorama import Back, Style, Fore

from .block import Block
from .settings import *
from .ball import Ball


class PowerUps(Block):
    """Parent class for the different powerups"""

    def __init__(self, x, y, otp):
        Block.__init__(self, x, y, 1, 0, otp)

    def doPowerUp(self, player, balls):
        pass

    def move(self, player, balls):
        self.x += self.velocity["x"]
        if self.x == BOARD_HEIGHT - 1:
            if self.y >= player.paddleLeft and self.y < player.paddleLeft + player.paddleLength:
                self.doPowerUp(player, balls)
            return False
        return True


class ExpandPaddle(PowerUps):
    """Power up to expand the player's paddle"""

    def __init__(self, x, y):
        PowerUps.__init__(self, x, y, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " E " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        player.paddleLength *= 2
        if player.paddleLength > MAX_PADDLE_LENGTH:
            player.paddleLength = MAX_PADDLE_LENGTH


class ShrinkPaddle(PowerUps):
    """Power up to shrink the player's paddle"""

    def __init__(self, x, y):
        PowerUps.__init__(self, x, y, Style.BRIGHT + Fore.BLACK +
                          Back.RED + " S " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        player.paddleLength = player.paddleLength // 2
        if player.paddleLength < MIN_PADDLE_LENGTH:
            player.paddleLength = MIN_PADDLE_LENGTH


class BallMultiplier(PowerUps):
    def __init__(self, x, y):
        PowerUps.__init__(self, x, y, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " B " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        newBalls = []
        for ball in balls:
            newBalls.append(
                Ball(ball.x, ball.y, ball.velocity["x"], -ball.velocity["y"], ball.thru_ball))
        for ball in newBalls:
            balls.append(ball)


class FastBall(PowerUps):
    """Power up to increase the speed of the ball"""

    def __init__(self, x, y):
        PowerUps.__init__(self, x, y, Style.BRIGHT + Fore.BLACK +
                          Back.RED + " F " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        for ball in balls:
            ball.velocity["y"] += 1
            if ball.velocity["y"] > MAX_BALL_VELOCITY:
                ball.velocity["y"] = MAX_BALL_VELOCITY


class ThruBall(PowerUps):
    """Power up to make the ball go through blocks"""

    def __init__(self, x, y):
        PowerUps.__init__(self, x, y, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " T " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        for ball in balls:
            ball.thru_ball = True


class PaddleGrab(PowerUps):
    """Power up to make the paddle grab the balls"""

    def __init__(self, x, y):
        PowerUps.__init__(self, x, y, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " G " + Style.RESET_ALL)

    def doPowerUp(self, player, balls):
        player.grabPaddle = True
