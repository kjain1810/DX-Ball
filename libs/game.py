from colorama import Back, Style
from time import sleep

from .input import Get, input_to
from .settings import *
from .output import clearscreen, outputboard, endgame, newlife
from .player import Player
from .utils import create_level
from .ball import Ball


class Game():
    """The main game class"""

    def __init__(self):
        self.getter = Get()
        self.player = Player()
        self.board_objects = create_level()
        self.balls = [Ball(
            BOARD_HEIGHT - 1, int(self.player.paddleLeft + self.player.paddleLength / 2), 0, 0)]
        self.game_board = self.construct_game_board()
        self.looper()

    def construct_game_board(self):
        """Constructs the board accotding to the objects"""
        ret = []
        for i in range(BOARD_HEIGHT):
            line = []
            for j in range(BOARD_WIDTH):
                line.append(Back.BLACK + " " * BLOCK_WIDTH + Style.RESET_ALL)
            ret.append(line)
        for i in range(self.player.paddleLeft, self.player.paddleLeft + self.player.paddleLength):
            ret[BOARD_HEIGHT - 1][i] = PADDLE_OUTPUT
        for obj in self.board_objects:
            ret[obj.x][obj.y] = obj.otp
        for ball in self.balls:
            ret[ball.x][ball.y] = ball.otp
        return ret

    def looper(self):
        """The main loop function"""
        while True:
            x = input_to(self.getter)
            if x == 'a':
                self.player.movePaddleLeft(self.balls)
            elif x == 'd':
                self.player.movePaddleRight(self.balls)
            elif x == 'w':
                for ball in self.balls:
                    if ball.velocity["x"] == 0:
                        ball.release(self.player.paddleLeft,
                                     self.player.paddleLength)
            elif x == 'q':
                print("Bye!")
                break
            for ball in self.balls:
                self.board_objects = [
                    obj for obj in self.board_objects if obj.collide(ball)]
            self.balls = [ball for ball in self.balls if ball.move(
                self.player.paddleLeft, self.player.paddleLength)]
            clearscreen()
            self.game_board = self.construct_game_board()
            outputboard(self.game_board, self.player)
            sleep(0.01/self.player.speed)
            if len(self.balls) == 0:
                self.player.reduceLife()
                if self.player.lives == 0:
                    endgame(self.player.score)
                    return
                else:
                    newlife(self.player.lives)
                    self.startNewLife()

    def startNewLife(self):
        """Starts a new life for the player"""
        self.balls = [Ball(
            BOARD_HEIGHT - 1, int(self.player.paddleLeft + self.player.paddleLength / 2), 0, 0)]
