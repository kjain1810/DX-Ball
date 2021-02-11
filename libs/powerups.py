from colorama import Back, Style, Fore

from .block import Block
from .settings import *


class PowerUps(Block):
    """Parent class for the different powerups"""

    def __init__(self, x, y, otp):
        Block.__init__(x, y, 1, 0, otp)


class ExpandPaddle(PowerUps):
    """Power up to expand the player's paddle"""

    def __init__(self, x, y):
        PowerUps.__init__(x, y, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " E " + Style.RESET_ALL)


class ShrinkPaddle(PowerUps):
    """Power up to shrink the player's paddle"""

    def __init__(self, x, y):
        PowerUps.__init__(x, y, Style.BRIGHT + Fore.BLACK +
                          Back.RED + " S " + Style.RESET_ALL)


class BallMultiplier(PowerUps):
    def __init__(self, x, y):
        PowerUps.__init__(x, y, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " B " + Style.RESET_ALL)


class FastBall(PowerUps):
    """Power up to increase the speed of the ball"""

    def __init__(self, x, y):
        PowerUps.__init__(x, y, Style.BRIGHT + Fore.BLACK +
                          Back.RED + " F " + Style.RESET_ALL)


class ThruBall(PowerUps):
    """Power up to make the ball go through blocks"""

    def __init__(self, x, y):
        PowerUps.__init__(x, y, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " T " + Style.RESET_ALL)


class PaddleGrab(PowerUps):
    """Power up to make the paddle grab the balls"""

    def __init__(self, x, y):
        PowerUps.__init__(x, y, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " G " + Style.RESET_ALL)
