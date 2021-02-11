from colorama import Back, Fore

from .block import Block
from .settings import *
from .debugger import debugger


class Ball(Block):
    """Class that defines the balls"""

    def __init__(self, x, y, velx, vely):
        Block.__init__(self, x, y, velx, vely, Back.WHITE + Fore.BLACK + "OOO")

    def release(self, paddleLeft, paddleLength):
        """Releases a ball that is resting on the paddle"""
        self.velocity["x"] = -1
        self.velocity["y"] = self.y - int(paddleLeft + paddleLength / 2)

    def move(self, paddleLeft, paddleLength):
        """Moves the balls according to their velocities"""
        self.x += self.velocity["x"]
        self.y += self.velocity["y"]
        if self.x < 0:
            self.x = 0
            self.velocity["x"] = -self.velocity["x"]
        if self.x >= BOARD_HEIGHT - 1:
            if self.y >= paddleLeft and self.y < paddleLeft + paddleLength:
                self.velocity["x"] = -self.velocity["x"]
                self.velocity["y"] = self.y - \
                    int(paddleLeft + paddleLength / 2)
                return True
            return False
        if self.y < 0:
            self.y = 0
            self.velocity["y"] = -self.velocity["y"]
        if self.y >= BOARD_WIDTH:
            self.y = BOARD_WIDTH - 1
            self.velocity["y"] = -self.velocity["y"]
        # debugger.debug(self.velocity)
        return True
