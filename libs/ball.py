from .block import Block

class Ball(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y, 0, -1)