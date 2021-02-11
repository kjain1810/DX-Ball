from colorama import Back, Style

from .block import Block
from .settings import *

levelColors = [None, Back.YELLOW, Back.BLUE, Back.RED]
totalLevels = 3
levelColors.append(Back.CYAN)


class Bricks(Block):
    """Class that defines each of the bricks"""

    def __init__(self, x, y, level, breakable=True):
        if level > totalLevels:
            level = totalLevels + 1
        Block.__init__(self, x, y, 0, 0, Style.DIM +
                       levelColors[level] + " " * BLOCK_WIDTH + Style.RESET_ALL)
        self.level = level
        self.breakable = breakable

    def collide(self, ball):
        """Tell if ball collides with bricks or not"""
        if abs(ball.x - self.x) == 1 and abs(ball.y - self.y) == 1:
            ball.velocity["x"] *= -1
            ball.velocity["y"] *= -1
        elif abs(ball.x - self.x) == 1:
            ball.velocity["x"] *= -1
        else:
            ball.velocity["y"] *= -1
        return self.takeHit()

    def dist(self, obj):
        """Return distance between brick and object"""
        return abs(self.x - obj.x) + abs(self.y - obj.y)

    def takeHit(self):
        """Reduce strenght of the brick"""
        if self.breakable == False:
            return False
        self.level -= 1
        if self.level == 0:
            return True
        self.otp = levelColors[self.level] + \
            " " * BLOCK_WIDTH + Style.RESET_ALL
        return False
