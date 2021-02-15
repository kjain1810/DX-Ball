import os
from time import sleep
from colorama import Style
from tabulate import tabulate

from .debugger import debugger
from .settings import *
from .ball import Ball
from .bricks import Bricks
from .powerups import ExpandPaddle, ShrinkPaddle, BallMultiplier, FastBall, ThruBall, PaddleGrab

instructions = [
    ["Paddle", PADDLE_OUTPUT + Style.RESET_ALL, "Paddle of the player"],
    ["Ball", Ball(0, 0, 0, 0).otp + Style.RESET_ALL, "Ball(s) of the player"],
    ["Unbreakable brick", Bricks(0, 0, 100, False).otp + Style.RESET_ALL,
     "Bricks that can not be broken without a thru ball"],
    ["Brick level 1", Bricks(0, 0, 1).otp + Style.RESET_ALL,
     "Brick that breaks with 1 hit, fetches 1 point"],
    ["Brick level 2", Bricks(0, 0, 2).otp + Style.RESET_ALL,
     "Brick that breaks with 2 hit, fetches 2 point"],
    ["Brick level 3", Bricks(0, 0, 3).otp + Style.RESET_ALL,
     "Brick that breaks with 3 hit, fetches 3 point"],
    ["Expand paddle", ExpandPaddle(
        0, 0).otp + Style.RESET_ALL, "Increases the paddle length"],
    ["Shrink paddle", ShrinkPaddle(
        0, 0).otp + Style.RESET_ALL, "Decreases the paddle length"],
    ["Grab paddle", PaddleGrab(0, 0).otp + Style.RESET_ALL,
     "Makes the paddle grab the ball everytime"],
    ["Ball multiplier", BallMultiplier(
        0, 0).otp + Style.RESET_ALL, "Doubles the number of balls present"],
    ["Fast ball", FastBall(0, 0).otp + Style.RESET_ALL,
     "Increases the speed of the ball(s)"],
    ["Thru ball", ThruBall(0, 0).otp + Style.RESET_ALL,
     "Makes the ball(s) go through everything except the paddle"]
]
instruction_header = ["Object", "Symbol", "Description"]
tabulated = tabulate(instructions, instruction_header, tablefmt="orgtbl")


def clearscreen():
    """Clears the screen"""
    os.system("clear")


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
    print("")
    print(tabulated)


def endgame(score):
    """Output when game ends"""
    clearscreen()
    print("GAME OVER!!!")
    print("SCORE: ", score)
    sleep(SLEEPTIME)


def newlife(player):
    """Output when life is lost"""
    clearscreen()
    print("LIFE OVER!!!")
    print("LIFES REMAINING: ", player.lives)
    player.paddleLength = INIT_PADDLE_LENGTH
    player.paddleLeft = int(BOARD_WIDTH / 2 - INIT_PADDLE_LENGTH)
    player.grabPaddle = 0
    sleep(SLEEPTIME)
    clearscreen()
