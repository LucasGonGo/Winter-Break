import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load('assets/images/background_1.png')

        self.bg_pos = [self.screen.get_width() // 2, self.screen.get_height() // 2]
        self.movement = [False, False]

    def run(self):
        while True:
            self.bg_pos[1] += (self.movement[1] - self.movement[0])

            self.screen.blit(self.background, self.bg_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

            pygame.display.update()
            self.clock.tick(60)

Game().run()