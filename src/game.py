import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load('assets/images/background_1.png')

        self.bg_pos = [self.screen.get_width() // 2, self.screen.get_height() // 2]
        self.movement = [False, False, False, False]

    def run(self):
        while True:
            self.screen.fill((14,219,248))

            if self.movement[0]:  # W
                self.bg_pos[1] -= 5
            if self.movement[1]:  # S
                self.bg_pos[1] += 5
            if self.movement[2]:  # A
                self.bg_pos[0] -= 5
            if self.movement[3]:  # D
                self.bg_pos[0] += 5

            self.screen.blit(self.background, self.bg_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                    if event.key == pygame.K_a:
                        self.movement[2] = True
                    if event.key == pygame.K_d:
                        self.movement[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False
                    if event.key == pygame.K_a:
                        self.movement[2] = False
                    if event.key == pygame.K_d:
                        self.movement[3] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()