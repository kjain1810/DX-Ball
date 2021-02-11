class Block():
    def __init__(self, x, y, velx, vely):
        self.x = x
        self.y = y
        self.velocity = {
            "x": velx,
            "y": vely
        }