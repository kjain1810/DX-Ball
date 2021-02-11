import subprocess as sp 
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