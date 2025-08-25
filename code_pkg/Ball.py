import pygame
from code_pkg.Const import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SPEED_1, BALL_SPEED_2

class Ball:
    def __init__(self):
        load_img = pygame.image.load('./asset/ball.png').convert_alpha()
        self.image = pygame.transform.scale(load_img, (15, 15))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.speed = [BALL_SPEED_1, BALL_SPEED_2]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed[0] *= -1
        if self.rect.top <= 0:
            self.speed[1] *= -1

