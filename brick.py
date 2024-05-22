# 플레이어가 깨야 하는 벽돌

import pygame


BLUE = (0, 0, 255)


class Brick:
    # 위치(x, y 좌표)
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 60, 20)
        self.hidden = False


    # 내구도 (깨지기 전 후 상태)
    # 벽돌 파괴 관련 메서드
    def draw(self, screen):
        if not self.hidden:
            pygame.draw.rect(screen, BLUE, self.rect)