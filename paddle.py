import pygame
from screen import SCREEN_WIDTH, SCREEN_HEIGHT

WHITE = (255, 255, 255)

class Paddle:
    def __init__(self, level):
        width = 100 - 10 * (level - 1)
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - width // 2, SCREEN_HEIGHT - 30, width, 10)
        self.speed = 6

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)