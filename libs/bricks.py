from colorama import Back, Style

from .block import Block
from .settings import *


class Bricks(Block):
    """Class that defines each of the bricks"""

    def __init__(self, x, y, level, breakable=False):
        if level == 1:
            self.color = Back.YELLOW
        elif level == 2:
            self.color = Back.BLUE
        elif level == 3:
            self.color = Back.RED
        elif breakable == True:
            self.color = Back.CYAN
        Block.__init__(self, x, y, 0, 0, Style.DIM +
                       self.color + " " * BLOCK_WIDTH + Style.RESET_ALL)
        self.level = level
        self.breakable = breakable

    def collide(self, ball):
        return True
