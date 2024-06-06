from brick import Brick

class Level:
    def __init__(self, level=1):
        self.level = level
        self.bricks = Brick.initialize_bricks(self.level)

    def level_up(self):
        self.level += 1
        self.bricks = Brick.initialize_bricks(self.level)