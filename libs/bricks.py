from .block import Block

class Bricks(Block):
    def __init__(self, x, y, level, breakable=False):
        Block.__init__(self, x, y, 0, 0)
        self.level = level
        self.breakable = breakable