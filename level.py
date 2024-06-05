from brick import Brick
from ball import Ball
from paddle import Paddle

class Level:
    def __init__(self, level=1):
        self.level = level
        self.bricks = Brick.initialize_bricks(self.level)

    def level_up(self, ball, paddle):
        self.level += 1  
        self.increase_speed(ball)  
        self.shorten(paddle) 
        self.bricks = Brick.initialize_bricks(self.level)
        
    def increase_speed(self, ball):
        ball.speed_x *= 1.1
        ball.speed_y *= 1.1
        
    def shorten(self, paddle):
        paddle.rect.width = max(30, paddle.rect.width - 10)