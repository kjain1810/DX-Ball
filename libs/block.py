from .settings import *
from .debugger import debugger


class Block():
    """The main block class which represents all objects not in user control"""

    def __init__(self, x, y, velx, vely, otp):
        self.x = x
        self.y = y
        self.velocity = {
            "x": velx,
            "y": vely
        }
        self.otp = otp

    def move(self):
        """Moves the object"""
        self.x += self.velocity["x"]
        self.y += self.velocity["y"]
        if self.x < 0:
            self.x = 0
            self.velocity["x"] = -self.velocity["x"]
        if self.x > BOARD_HEIGHT - 1:
            return False
        if self.y < 0:
            self.y = 0
            self.velocity["y"] = -self.velocity["y"]
        if self.y >= BOARD_WIDTH:
            self.y = BOARD_WIDTH - 1
            self.velocity["y"] = -self.velocity["y"]
        return True
