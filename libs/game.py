from .input import Get, input_to
from .settings import *
from .output import clearscreen, outputboard

class Game():
    def __init__(self):
        self.game_board = self.construct_game_board()
        self.left_end = int(BOARD_WIDTH / 2 - 5)
        self.right_end = int(BOARD_WIDTH / 2 + 4)
        self.getter = Get()
        self.looper()
    
    def construct_game_board(self):
        ret = []
        for i in range(BOARD_HEIGHT - 1):
            line = []
            for j in range(BOARD_WIDTH):
                line.append('.')
            ret.append(line)
        line = []
        for j in range(int(BOARD_WIDTH / 2) - 5):
            line.append('.')
        for j in range(10):
            line.append('_')
        for j in range(int(BOARD_WIDTH / 2) - 5):
            line.append('.')
        ret.append(line)
        return ret
    def looper(self):
        while True:
            x = input_to(self.getter)
            if x == 'a':
                self.game_board[BOARD_HEIGHT - 1][self.left_end - 1] = '_'
                self.game_board[BOARD_HEIGHT - 1][self.right_end] = '.'
                self.left_end -= 1
                self.right_end -= 1
            elif x == 'd':
                self.game_board[BOARD_HEIGHT - 1][self.left_end] = '.'
                self.game_board[BOARD_HEIGHT - 1][self.right_end + 1] = '_'
                self.left_end += 1
                self.right_end += 1
            elif x == 'q':
                print("Bye!")
                break
            clearscreen()
            outputboard(self.game_board)