import pygame
import sys
from code_pkg.Const import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, FONT, FONT_SIZE

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(name=FONT, size=FONT_SIZE)

    def run(self):
        # Display the menu until SPACE is pressed.
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return  # start game

            self.screen.fill((30, 30, 30))
            title_surf = self.font.render("Brick Breaker", True, (255, 255, 255))
            instr_surf = self.font.render("Press SPACE to Play", True, (200, 200, 200))
            self.screen.blit(title_surf, title_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 40)))
            self.screen.blit(instr_surf, instr_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40)))
            pygame.display.flip()
            clock.tick(FPS)
            