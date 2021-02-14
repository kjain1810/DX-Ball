import subprocess as sp
from time import sleep
from colorama import Style

from .debugger import debugger
from .settings import *
from .ball import Ball
from .bricks import Bricks
from .powerups import ExpandPaddle, ShrinkPaddle, BallMultiplier, FastBall, ThruBall, PaddleGrab


def clearscreen():
    """Clears the screen"""
    sp.call('clear', shell=True)


def outputboard(board, player):
    """Outputs the board"""
    for row in board:
        for cell in row:
            print(cell, end="")
        print("")
    print(Style.RESET_ALL)

    # Player information
    text_space = len("Lives: " + str(player.lives) + "Score: " +
                     str(player.score) + "Time: " + str(player.time))
    empty_space = BOARD_WIDTH * BLOCK_WIDTH - text_space
    print("Lives:", player.lives, end="")
    for i in range(int(empty_space//2)):
        print(" ", end="")
    print("Score:", player.score, end="")
    for i in range(int(empty_space//2)):
        print(" ", end="")
    print("Time:", player.time)

    # Game instructions
    print("Block instructions:")
    print("Paddle:", PADDLE_OUTPUT + Style.RESET_ALL)
    print("Ball:", Ball(0, 0, 0, 0).otp + Style.RESET_ALL)
    print("Unbreakable brick:", Bricks(0, 0, 100, False).otp + Style.RESET_ALL)
    print("Brick level 1:", Bricks(0, 0, 1).otp + Style.RESET_ALL)
    print("Brick level 2:", Bricks(0, 0, 2).otp + Style.RESET_ALL)
    print("Brick level 3:", Bricks(0, 0, 3).otp + Style.RESET_ALL)
    print("Expand paddle:", ExpandPaddle(0, 0).otp + Style.RESET_ALL)
    print("Shrink paddle:", ShrinkPaddle(0, 0).otp + Style.RESET_ALL)
    print("Grab paddle:", PaddleGrab(0, 0).otp + Style.RESET_ALL)
    print("Ball multiplier:", BallMultiplier(0, 0).otp + Style.RESET_ALL)
    print("Fast ball:", FastBall(0, 0).otp + Style.RESET_ALL)
    print("Thru ball:", ThruBall(0, 0).otp + Style.RESET_ALL)
    # debugger.printDebugs()


def endgame(score):
    """Output when game ends"""
    clearscreen()
    print("GAME OVER!!!")
    print("SCORE: ", score)
    sleep(SLEEPTIME)


def newlife(lives):
    """Output when life is lost"""
    clearscreen()
    print("LIFE OVER!!!")
    print("LIFES REMAINING: ", lives)
    sleep(SLEEPTIME)
    clearscreen()
