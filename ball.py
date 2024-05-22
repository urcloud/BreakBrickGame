# 벽돌을 깨는 공


import pygame
import random
from screen import SCREEN_WIDTH, SCREEN_HEIGHT


RED = (255, 0, 0)


class Ball:
    # 위치 (x, y 좌표)
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10, 10)
        self.speed_x = 4 * random.choice((1, -1))
        self.speed_y = 4 * random.choice((1, -1))


    # 이동방향
    # 이동 관련 메서드
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1


    def collide_with_paddle(self, paddle_rect):
        if self.rect.colliderect(paddle_rect):
            self.speed_y *= -1


    def collide_with_bricks(self, bricks):
        hit_index = self.rect.collidelist(bricks)
        if hit_index != -1:
            bricks.pop(hit_index)
            self.speed_y *= -1
            return True
        return False


    def draw(self, screen):
        pygame.draw.ellipse(screen, RED, self.rect)
