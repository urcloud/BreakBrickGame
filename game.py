import pygame
import time
from ball import Ball
from paddle import Paddle
from brick import Brick
from screen import Screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from collision import detect_collision
from level import Level
import admin

class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.ball = Ball(self.level.level)
        self.paddle = Paddle(self.level.level)
        self.running = False
        self.paused = False
        self.score = 0
        self.lives = 3
        self.player_name = None
        self.level.bricks = Brick.initialize_bricks(self.level.level)

    def get_player_name(self):
        name = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode
            self.screen.fill(BLACK)
            self.screen.draw_text("Enter your name:", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            self.screen.draw_text(name, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            self.clock.tick(30)

    def run(self):
        self.player_name = self.get_player_name()
        self.running = True
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
            if detect_collision(self.ball, self.paddle, self.level.bricks):
                self.score += 10

            if self.ball.rect.bottom >= SCREEN_HEIGHT:
                self.lives -= 1
                if self.lives > 0:
                    self.ball = Ball(self.level.level)
                    self.paddle = Paddle(self.level.level)
                else:
                    self.running = False

            if not self.level.bricks:
                self.level.level_up()
                self.ball = Ball(self.level.level)
                self.paddle = Paddle(self.level.level)
                self.wait_for_level_up()
                
    def wait_for_level_up(self):
        self.screen.fill(BLACK)
        self.screen.draw_text("Level Up!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.update()
        pygame.time.wait(1000)

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.draw(self.paddle, self.ball, *self.level.bricks)
        self.screen.draw_text(f"Score: {self.score}", (150, 10))
        self.screen.draw_text(f"Level: {self.level.level}", (10, 10))
        self.screen.draw_text(f"Lives: {self.lives}", (SCREEN_WIDTH - 150, 10))
        if self.running:
            self.screen.draw_text(f"Player: {self.player_name}", (10, SCREEN_HEIGHT - 30))
        if self.paused:
            self.screen.draw_text("Paused", (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
        self.screen.update()

    def show_game_over_screen(self):
        self.screen.fill(BLACK)
        game_over_font = pygame.font.Font(None, 50)
        score_font = pygame.font.Font(None, 36)
        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        score_text = score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        player_text = score_font.render(f"Player: {self.player_name}", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        player_rect = player_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.screen.blit(game_over_text, game_over_rect)
        self.screen.screen.blit(score_text, score_rect)
        self.screen.screen.blit(player_text, player_rect)
        self.screen.draw_text("Press R to play again or Q to quit", (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()
        admin.save_user_data(self.player_name, self.score, self.level.level)
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
        self.level = Level()
        self.score = 0
        self.lives = 3
        self.running = True
        self.level.bricks = Brick.initialize_bricks(self.level.level)
        self.ball = Ball(self.level.level)
        self.paddle = Paddle(self.level.level)