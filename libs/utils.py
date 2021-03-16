from random import random

from .settings import *
from .bricks import Bricks
from .powerups import *


def create_level(level):
    """Creates the initial level"""
    if level == 0:
        ret = []
        for i in range(3):
            level = 3 - i
            y = i
            for j in range(BOARD_WIDTH):
                ret.append(Bricks(y, j, level))
        for i in range(10, BOARD_WIDTH - 10):
            ret.append(Bricks(3, i, 10000, False))
        return ret
    elif level == 1:
        ret = []
        for i in range(BOARD_WIDTH):
            ret.append(Bricks(0, i, 3))
        for i in range((BOARD_WIDTH - 10) // 2):
            ret.append(Bricks(1, i, 2))
            ret.append(Bricks(1, BOARD_WIDTH - i - 1, 2))
        for i in range((BOARD_WIDTH - 10) // 2, BOARD_WIDTH - (BOARD_WIDTH - 10) // 2):
            ret.append(Bricks(1, i, 10000, False))
        for i in range((BOARD_WIDTH - 20) // 2):
            ret.append(Bricks(2, i, 1))
            ret.append(Bricks(2, BOARD_WIDTH - i - 1, 1))
        for i in range((BOARD_WIDTH - 20) // 2, BOARD_WIDTH - (BOARD_WIDTH - 20) // 2):
            ret.append(Bricks(2, i, 10000, False))
        return ret
    else:
        # boss level
        pass


def create_test_level_0():
    """A test level"""
    ret = []
    ret.append(Bricks(0, 19, 1))
    return ret


def get_powerup(x, y):
    """Determines if brick should release powerup or not"""
    num = random()
    summation = 0
    summation += PROB_BALL_FAST
    if summation >= num:
        return FastBall(x, y)
    summation += PROB_BALL_MULTIPLIER
    if summation >= num:
        return BallMultiplier(x, y)
    summation += PROB_BALL_THRU
    if summation >= num:
        return ThruBall(x, y)
    summation += PROB_PADDLE_EXPAND
    if summation >= num:
        return ExpandPaddle(x, y)
    summation += PROB_PADDLE_GRAB
    if summation >= num:
        return PaddleGrab(x, y)
    summation += PROB_PADDLE_SHRINK
    if summation >= num:
        return ShrinkPaddle(x, y)
    return None
