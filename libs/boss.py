from colorama import Style, Back, Fore

from .settings import *
from .bricks import Bricks, InvisibleBricks


class Boss():
    def __init__(self):
        self.objs = []
        self.strength = 100
        self.leftEdge = BOARD_WIDTH // 2 - 7
        self.rightEdge = BOARD_WIDTH // 2 + 3
        for i in range(self.leftEdge, self.rightEdge):
            self.objs.append(Bricks(0, i, 10000, False))
            self.objs.append(Bricks(3, i, 10000, False))
        for i in range(self.leftEdge + 1, self.rightEdge - 1):
            self.objs.append(InvisibleBricks(2, i))
        for i in range(self.leftEdge + 1, (self.leftEdge + self.rightEdge) // 2):
            self.objs.append(InvisibleBricks(1, i))
        for i in range((self.leftEdge + self.rightEdge) // 2 + 1, self.rightEdge - 1):
            self.objs.append(InvisibleBricks(1, i))
        for i in range(1, 3):
            self.objs.append(Bricks(i, self.leftEdge, 10000, False))
            self.objs.append(Bricks(i, self.rightEdge - 1, 10000, False))
        self.minions = []

    def move(self, y):
        if self.leftEdge + y < 0:
            y = -self.leftEdge
        elif self.rightEdge + y >= BOARD_WIDTH:
            y = BOARD_WIDTH - self.rightEdge
        self.leftEdge += y
        self.rightEdge += y
        for obj in self.objs:
            obj.y += y

    def check_collide(self, ball):
        pass

    def get_objects(self):
        ret = []
        for obj in self.objs:
            ret.append(obj)
        for minion in self.minions:
            ret.append(minion)
        return ret

    def reset_position(self):
        y = BOARD_WIDTH // 2 - 7 - self.leftEdge
        self.leftEdge += y
        self.rightEdge += y
        for obj in self.objs:
            obj.y += y

    def decrease_life(self):
        self.strength -= 1
        return self.strength > 0
