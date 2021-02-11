import subprocess as sp
from time import sleep
from colorama import Style

from .debugger import debugger


def clearscreen():
    sp.call('clear', shell=True)


def outputboard(board, player):
    for row in board:
        for cell in row:
            print(cell, end="")
        print("")
    print(Style.RESET_ALL)
    print("Lives: ", player.lives)
    print("Score: ", player.score)
    print("Time: ", player.time)
    debugger.printDebugs()


def endgame(score):
    clearscreen()
    print("GAME OVER!!!")
    print("SCORE: ", score)
    sleep(5)
    exit()


def newlife(lives):
    clearscreen()
    print("LIFE OVER!!!")
    print("LIFES REMAINING: ", lives)
    sleep(5)
    clearscreen()
