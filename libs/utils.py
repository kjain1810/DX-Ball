from .settings import *
from .bricks import Bricks


def create_level():
    """Creates the initial level"""
    ret = []
    for i in range(3):
        level = 3 - i
        y = i
        for j in range(BOARD_WIDTH):
            ret.append(Bricks(y, j, level))
    for i in range(5, BOARD_WIDTH - 5):
        ret.append(Bricks(3, i, 10000, False))
    return ret


def create_test_level_0():
    ret = []
    for i in range(7):
        ret.append(Bricks(i, 25, 10000, False))
    return ret
