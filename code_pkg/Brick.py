import pygame

class Brick:
    def __init__(self, position):
        self.image = pygame.image.load('./asset/brick.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
