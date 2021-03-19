from colorama import Fore, Back, Style

from .block import Block
from .settings import *


class Bombs(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y, 1, 0, Back.RED + " " *
                       BLOCK_WIDTH + Style.RESET_ALL,)

    def move(self, player):
        self.x += self.velocity["x"]
        if self.x == BOARD_HEIGHT - 1:
            if player.paddleLeft <= self.y and player.paddleLeft + player.paddleLength - 1 >= self.y:
                return True
            return False
