from colorama import Back, Style
from time import sleep

from .input import Get, input_to
from .settings import *
from .output import clearscreen, outputboard, endgame, newlife, printWinner, showLevelUp
from .player import Player
from .utils import create_level, get_powerup
from .ball import Ball
from .debugger import debugger
from .boss import Boss

from .utils import create_test_level_0


class Game():
    """The main game class"""

    def __init__(self):
        self.getter = Get()
        self.player = Player()
        self.board_objects = create_level(0)
        self.balls = [Ball(
            BOARD_HEIGHT - 1, int(self.player.paddleLeft + self.player.paddleLength / 2), 0, 0)]
        self.powerups = []
        self.bullets = []
        self.boss = Boss()
        self.game_board = self.construct_game_board()
        self.looper()

    def assing_obj(self, board, obj):
        """Assing a position on the board if possible"""
        if obj.x < 0 or obj.y < 0:
            return False
        if obj.x >= BOARD_HEIGHT or obj.y >= BOARD_WIDTH:
            return False
        board[obj.x][obj.y] = obj.otp
        return True

    def construct_game_board(self):
        """Constructs the board accotding to the objects"""
        ret = []
        for i in range(BOARD_HEIGHT):
            line = []
            for j in range(BOARD_WIDTH):
                line.append(Back.BLACK + " " * BLOCK_WIDTH + Style.RESET_ALL)
            ret.append(line)
        ret = self.player.setPaddleOutput(ret)
        self.board_objects = [
            obj for obj in self.board_objects if self.assing_obj(ret, obj)]
        self.balls = [
            ball for ball in self.balls if self.assing_obj(ret, ball)]
        self.powerups = [
            powerup for powerup in self.powerups if self.assing_obj(ret, powerup)]
        self.bullets = [
            bullet for bullet in self.bullets if self.assing_obj(ret, bullet)]
        if self.player.level == BOSS_LEVEL:
            x = 1
            y = (self.boss.leftEdge + self.boss.rightEdge) // 2
            if self.boss.strength == 100:
                ret[x][y] = Back.BLACK + Fore.WHITE + "100" + Style.RESET_ALL
            elif self.boss.strength >= 10:
                ret[x][y] = Back.BLACK + Fore.WHITE + \
                    str(int(self.boss.strength)) + " " + Style.RESET_ALL
            else:
                ret[x][y] = Back.BLACK + Fore.WHITE + " " + \
                    str(int(self.boss.strength)) + " " + Style.RESET_ALL
        return ret

    def looper(self):
        """The main loop function"""
        while True:
            x = input_to(self.getter, self.player.speed)
            if x == 'a':
                self.player.movePaddleLeft(self.balls)
                if self.player.level == BOSS_LEVEL:
                    self.boss.move(-2)
            elif x == 'd':
                self.player.movePaddleRight(self.balls)
                if self.player.level == BOSS_LEVEL:
                    self.boss.move(2)
            elif x == 'w':
                for ball in self.balls:
                    if ball.velocity["x"] == 0:
                        ball.release(self.player.paddleLeft,
                                     self.player.paddleLength)
                if self.player.shootingPaddle:
                    self.player.makeShot(self.bullets)
            elif x == 'q':
                print("Bye!")
                break

            if self.player.level == BOSS_LEVEL:
                self.board_objects = self.boss.get_objects()

            # MOVE BULLETS
            obj_torem = []
            bullet_torem = []
            for bullet in self.bullets:
                for obj in self.board_objects:
                    if bullet.x == obj.x and bullet.y == obj.y:
                        torem = obj.takeHit()
                        if torem:
                            obj_torem.append(obj)
                        bullet_torem.append(bullet)
                        if self.player.level == BOSS_LEVEL and obj.breakable == False:
                            if self.boss.decrease_life() == False:
                                printWinner()
                                return
            self.bullets = [
                bullet for bullet in self.bullets if bullet not in bullet_torem]
            self.bullets = [bullet for bullet in self.bullets if bullet.move()]
            self.board_objects = [
                obj for obj in self.board_objects if obj not in obj_torem]

            # MOVE BALLS
            obj_torem = []
            for ball in self.balls:
                can_collide = []
                for obj in self.board_objects:
                    if ball.can_collide(obj):
                        can_collide.append(obj)
                if len(can_collide) == 0:
                    continue
                if ball.thru_ball > 0:
                    for obj in can_collide:
                        obj_torem.append(obj)
                        newPowerUp = get_powerup(
                            obj.x, obj.y, ball.velocity["y"], self.player.level)
                        if newPowerUp != None:
                            self.powerups.append(newPowerUp)
                        self.player.increaseScore(obj.points)
                    continue
                does_collide = can_collide[0]
                if len(can_collide) == 2:
                    if can_collide[1].dist(ball) < does_collide.dist(ball):
                        does_collide = can_collide[1]
                if len(can_collide) == 3:
                    if can_collide[1].dist(ball) == 2:
                        does_collide = can_collide[1]
                    elif can_collide[2].dist(ball) == 2:
                        does_collide = can_collide[2]
                if self.player.level == BOSS_LEVEL and does_collide.breakable == False:
                    if self.boss.decrease_life() == False:
                        printWinner()
                        return
                if does_collide.collide(ball) == True:
                    obj_torem.append(does_collide)
                    self.player.increaseScore(does_collide.points)
                    newPowerUp = get_powerup(
                        does_collide.x, does_collide.y, ball.velocity["y"], self.player.level)
                    if newPowerUp != None:
                        self.powerups.append(newPowerUp)
            self.board_objects = [
                obj for obj in self.board_objects if obj not in obj_torem]
            ballstoremove = [ball for ball in self.balls if ball.move(
                self.player.paddleLeft, self.player.paddleLength, self.board_objects, self.player.grabPaddle, self.player.fallingBricks) == False]

            # MOVE POWERUPS
            self.powerups = [
                powerup for powerup in self.powerups if powerup.move(self.player, self.balls)]

            # DO TIME STUFF
            self.player.setTime(self.board_objects)

            # PRINT
            clearscreen()
            self.game_board = self.construct_game_board()
            outputboard(self.game_board, self.player)

            # RECALCULATE BALLS AND POWERUPS
            self.balls = [
                ball for ball in self.balls if ball not in ballstoremove]
            self.player.checkPowerUps()

            # GAME OVER DUE TO FALLING BRICKS
            for obj in self.board_objects:
                if obj.x >= BOARD_HEIGHT - 1:
                    endgame(self.player.score)
                    return

            # LIFE OVER
            if len(self.balls) == 0:
                sleep(1)
                self.player.reduceLife()
                if self.player.lives == 0:
                    endgame(self.player.score)
                    return
                else:
                    newlife(self.player)
                    self.startNewLife()
                    self.boss.reset_position()

            # LEVEL COMPLETED
            if len(self.board_objects) == 0:
                self.player.level += 1
                showLevelUp()
                self.resetLevel()

    def resetLevel(self):
        self.board_objects = create_level(self.player.level)
        self.player.resetLevel()
        self.balls = [Ball(
            BOARD_HEIGHT - 1, int(self.player.paddleLeft + self.player.paddleLength / 2), 0, 0)]
        self.powerups = []
        self.game_board = self.construct_game_board()

    def startNewLife(self):
        """Starts a new life for the player"""
        self.balls = [Ball(
            BOARD_HEIGHT - 1, int(self.player.paddleLeft + self.player.paddleLength / 2), 0, 0)]
