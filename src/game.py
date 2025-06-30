import pygame

import sys

from scripts.entities import PhysicsEntity
from scripts.utils import load_image

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Winter Break Project') # muda o nome na janela
        self.screen = pygame.display.set_mode((1280, 720))
        
        self.clock = pygame.time.Clock()

        self.movement = [False, False, False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (15, 15))

    def run(self):
        while True:
            self.screen.fill((14,219,248))

            self.player.update((self.movement [1] - self.movemen[0]), (self.movement[3] - self.movement[2]))
            self.render(self.screen, )

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