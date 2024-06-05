import random
from brick import Brick
from ball import Ball
from paddle import Paddle

class Level:
    def __init__(self, level=1):
        self.level = level
        self.bricks = self.initialize_bricks()

    def level_up(self, ball, paddle):
        self.level += 1  
        ball.increase_speed()  
        paddle.shorten() 
        self.bricks = self.initialize_bricks()
        
    def initialize_bricks(self):
        brick_count = self.level 
        brick_positions = [(random.randint(0, 9) * (60 + 10) + 35, random.randint(0, 9) * (20 + 10) + 35) for _ in range(brick_count)]
        return [Brick(x, y, self.level) for x, y in brick_positions]