import pygame
import random
from screen import SCREEN_WIDTH, SCREEN_HEIGHT

RED = (255, 0, 0)

class Ball:
    def __init__(self, level):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10, 10)
        self.speed_x = random.choice([-1, 1]) * (4 + 0.4 * (level-1))
        self.speed_y = random.choice([-1, 1]) * (4 + 0.4 * (level-1))

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, RED, self.rect)