from brick import Brick
from ball import Ball
from paddle import Paddle

class Level:
    def __init__(self, level=1):
        self.level = level
        self.bricks = Brick.initialize_bricks(self.level)

    def level_up(self, ball, paddle):
        self.level += 1  
        ball.increase_speed()  
        paddle.shorten() 
        self.bricks = Brick.initialize_bricks(self.level)