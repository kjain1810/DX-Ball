from colorama import Back, Fore

from .block import Block
from .settings import *
from .debugger import debugger


class Ball(Block):
    """Class that defines the balls"""

    def __init__(self, x, y, velx, vely, thru_ball=False):
        Block.__init__(self, x, y, velx, vely, Back.WHITE + Fore.BLACK + "OOO")
        self.thru_ball = thru_ball

    def release(self, paddleLeft, paddleLength):
        """Releases a ball that is resting on the paddle"""
        self.velocity["x"] = -1
        self.velocity["y"] = self.y - int(paddleLeft + paddleLength / 2)

    def move(self, paddleLeft, paddleLength, objects, grabPaddle):
        """Moves the balls according to their velocities"""
        if self.velocity["x"] == 0:
            return True
        self.x += self.velocity["x"]
        oldy = self.y
        self.y += self.velocity["y"]
        if self.thru_ball == False:
            for obj in objects:
                if obj.x == self.x and obj.y > oldy and obj.y <= self.y and self.velocity["y"] > 0:
                    self.y = obj.y - 1
                elif obj.x == self.x and obj.y < oldy and obj.y >= self.y and self.velocity["y"] < 0:
                    self.y = obj.y + 1
        if self.x < 0:
            self.x = 0
            self.velocity["x"] = -self.velocity["x"]
        if self.x >= BOARD_HEIGHT - 1:
            if self.y >= paddleLeft and self.y < paddleLeft + paddleLength:
                if grabPaddle:
                    self.velocity["x"] = 0
                    self.velocity["y"] = 0
                else:
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
        return True

    def can_collide(self, obj):
        """Tell if ball is about to collide with object"""
        if abs(obj.x - self.x) > 1:
            return False
        if abs(obj.y - self.y) > 1:
            return False
        if abs(obj.x - self.x) == 1 and abs(obj.y - self.y) == 1:
            if self.x + (self.velocity["x"]/abs(self.velocity["x"]) if self.velocity["x"] != 0 else 0) != obj.x or self.y + (self.velocity["y"]/abs(self.velocity["y"]) if self.velocity["y"] != 0 else 0) != obj.y:
                return False
            return True
        if abs(obj.x - self.x) == 1:
            if self.x + (self.velocity["x"]/abs(self.velocity["x"]) if self.velocity["x"] != 0 else 0) == obj.x:
                return True
            return False
        if abs(obj.y - self.y) == 1:
            if self.y + (self.velocity["y"]/abs(self.velocity["y"]) if self.velocity["y"] != 0 else 0) == obj.y:
                return True
            return False
