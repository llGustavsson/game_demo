import pygame
import sys
from code_pkg.Menu import Menu
from code_pkg.Paddle import Paddle
from code_pkg.Ball import Ball
from code_pkg.Brick import Brick
from code_pkg.Const import SCREEN_WIDTH, SCREEN_HEIGHT, FONT, FONT_SIZE, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Brick Breaker")
        self.clock = pygame.time.Clock()

        # Load game objects
        self.bricks = self.create_bricks()

    def create_bricks(self):
        bricks = []
        for row in range(5):
            for col in range(10):
                x = col * 100 
                y = row * 40
                bricks.append(Brick((x, y)))
        return bricks

    def reset_game(self):
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = self.create_bricks()

    def run_game(self):
        self.reset_game()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            self.ball.update()

            # Ball collision with paddle
            if self.ball.rect.colliderect(self.paddle.rect):
                self.ball.speed[1] *= -1

            # Ball collision with bricks
            for brick in self.bricks[:]:
                if self.ball.rect.colliderect(brick.rect):
                    self.bricks.remove(brick)
                    self.ball.speed[1] *= -1
                    break

            # Ball falls below screen → back to menu
            if self.ball.rect.bottom >= SCREEN_HEIGHT:
                return

            # Drawing
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.paddle.image, self.paddle.rect)
            self.screen.blit(self.ball.image, self.ball.rect)
            for brick in self.bricks:
                self.screen.blit(brick.image, brick.rect)
            pygame.display.flip()
            self.clock.tick(FPS)

    def run(self):
        menu = Menu(self.screen)
        while True:
            menu.run()
            self.run_game()
