import pygame
import sys
from code_pkg.Menu import Menu
from code_pkg.Paddle import Paddle
from code_pkg.Ball import Ball
from code_pkg.Brick import Brick
from code_pkg.Const import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, FONT, FONT_SIZE

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Brick Breaker")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(name=FONT, size=FONT_SIZE)
        
        # Load a music in loop
        pygame.mixer.init()
        pygame.mixer.music.load('./asset/music.mp3')
        pygame.mixer.music.play(-1)

    def create_bricks(self):
        bricks = []
        for row in range(10):
            for col in range(27):
                x = col * 35
                y = row * 20
                bricks.append(Brick((x, y)))
        return bricks
    
    def show_victory(self):
        self.screen.fill((46, 210, 46))
        title_surf = self.font.render("You WON!", True, (255, 255, 255))
        instr_surf = self.font.render("Press SPACE to Play", True, (200, 200, 200))
        self.screen.blit(title_surf, title_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 40)))
        self.screen.blit(instr_surf, instr_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40)))
        pygame.display.flip()
        self.clock.tick(FPS)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return

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
                
                if not self.bricks:
                    self.show_victory()
                    return

            # Ball falls below screen - Game Over - back to menu
            if self.ball.rect.bottom >= SCREEN_HEIGHT:
                while True :
                    self.screen.fill((210, 46, 46))
                    title_surf = self.font.render("GAME OVER", True, (255, 255, 255))
                    instr_surf = self.font.render("Press SPACE to Play", True, (200, 200, 200))
                    self.screen.blit(title_surf, title_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 40)))
                    self.screen.blit(instr_surf, instr_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40)))
                    pygame.display.flip()
                    self.clock.tick(FPS)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
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
