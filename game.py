# 게임상태 (진행중, 일시정지, 종료)
# 플레이어 정보 (점수, 목숨)


# 게임 시작, 일시정지, 재시작, 종료 관련 메서드
# 점수 업데이트, 플레이어 목숨 감소 등 상태변화 관련 메서드

import pygame
import time
import random
from ball import Ball
from brick import Brick
from paddle import Paddle
from screen import Screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from collision import detect_collision

class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.clock = pygame.time.Clock()
        self.level = 1
        self.ball = Ball()
        self.paddle = Paddle()
        self.bricks = []
        self.initialize_bricks()
        self.running = True
        self.paused = False
        self.score = 0
        self.lives = 3

    def initialize_bricks(self):
        brick_count = self.level 
        brick_positions = [(random.randint(0, 9) * (60 + 10) + 35, random.randint(0, 9) * (20 + 10) + 35) for _ in range(brick_count)]
        self.bricks = [Brick(x, y, self.level) for x, y in brick_positions]
    
    def reset_ball_and_paddle(self):
        self.ball = Ball(self.ball.speed_x, self.ball.speed_y) 
        self.paddle = Paddle(self.paddle.rect.width) 


    def run(self):
        self.countdown()
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        self.show_game_over_screen()

    def countdown(self):
        for i in range(3, 0, -1):
            self.screen.fill(BLACK)
            self.screen.draw_text(f"Game starts in {i}...", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.update()
            time.sleep(1)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused

    def update(self):
        if not self.paused:
            keys = pygame.key.get_pressed()
            self.paddle.move(keys)
            self.ball.move()
            if detect_collision(self.ball, self.paddle, self.bricks):
                self.score += 10

            if self.ball.rect.bottom >= SCREEN_HEIGHT:
                self.lives -= 1
                if self.lives > 0:
                    self.reset_ball_and_paddle()
                else:
                    self.running = False

            if not self.bricks:
                self.level += 1  
                self.ball.increase_speed()  
                self.paddle.shorten() 
                self.initialize_bricks() 
                self.reset_ball_and_paddle() 
                self.wait_for_level_up()
                
    def wait_for_level_up(self):
        self.screen.fill(BLACK)
        self.screen.draw_text("Level Up!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.update()
        pygame.time.wait(1000)

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.draw(self.paddle, self.ball, *self.bricks)
        self.screen.draw_text(f"Score: {self.score}", (150, 10))
        self.screen.draw_text(f"Level: {self.level}", (10, 10))
        self.screen.draw_text(f"Lives: {self.lives}", (SCREEN_WIDTH - 150, 10))
        if self.paused:
            self.screen.draw_text("Paused", (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
        self.screen.update()

    def show_game_over_screen(self):
        self.screen.fill(BLACK)
        game_over_font = pygame.font.Font(None, 50)
        score_font = pygame.font.Font(None, 36)
        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        score_text = score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.screen.blit(game_over_text, game_over_rect)
        self.screen.screen.blit(score_text, score_rect)
        self.screen.draw_text("Press R to play again or Q to quit", (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()
                        self.run()
                        waiting = False
                    elif event.key == pygame.K_q:
                        waiting = False
                        self.running = False


    def restart_game(self):
        self.level = 1 
        self.score = 0  
        self.running = True
        self.initialize_bricks() 
        self.reset_ball_and_paddle() 