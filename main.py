import os
import signal
from libs.game import Game

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    os.system('setterm -cursor off')
    Game()
    os.system('setterm -cursor on')
