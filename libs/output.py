import subprocess as sp 

def clearscreen():
    sp.call('clear', shell=True)

def outputboard(board):
    for row in board:
        for cell in row:
            print(cell, end="")
        print("")