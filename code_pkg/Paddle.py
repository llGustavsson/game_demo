import pygame
from code_pkg.Const import SCREEN_WIDTH, SCREEN_HEIGHT

class Paddle:
    def __init__(self):
        self.image = pygame.image.load('./asset/paddle.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 40))
        self.speed = 6

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
