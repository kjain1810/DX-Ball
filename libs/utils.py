from random import random

from .settings import *
from .bricks import Bricks
from .powerups import *


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
    """A test level"""
    ret = []
    for i in range(7):
        ret.append(Bricks(i, 25, 10000, False))
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
