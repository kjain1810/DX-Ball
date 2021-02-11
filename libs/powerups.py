from colorama import Back, Style, Fore

from .block import Block
from .settings import *


class PowerUps(Block):
    def __init__(self, x, y, otp):
        Block.__init__(x, y, 1, 0, otp)


class ExpandPaddle(PowerUps):
    def __init__(self, x, y):
        PowerUps.__init__(x, y, Style.BRIGHT + Fore.BLACK +
                          Back.GREEN + " E " + Style.RESET_ALL)


class ShrinkPaddle(PowerUps):
    def __init__(self, x, y):
        PowerUps.__init__(x, y, Style.BRIGHT + Fore.BLACK +
                          Back.RED + " S " + Style.RESET_ALL)
