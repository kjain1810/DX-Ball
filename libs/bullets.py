from colorama import Fore, Back, Style

from .block import Block
from .settings import *


class Bullet(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y, -1, 0, Style.BRIGHT + Fore.BLACK +
                       Back.RED + "===" + Style.RESET_ALL)

    def move(self):
        self.x += self.velocity["x"]
        if self.x > BOARD_HEIGHT - 1 or self.x < 0:
            return False
        return True
