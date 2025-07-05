import pygame

import sys

from scripts.entities import PhysicsEntity
from scripts.utils import load_image
from background import Background

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Winter Break Project') # muda o nome na janela
        self.screen = pygame.display.set_mode((1024, 768),  (pygame.RESIZABLE | pygame.SCALED))

        self.display = pygame.Surface((512, 384))
        
        self.background = Background(self.display)

        self.clock = pygame.time.Clock()

        self.movement = [False, False, False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (self.display.get_width()//2 , self.display.get_height()//2), (32, 32))

    def run(self):
        while True:

            self.display.fill((36,0,70))
            self.background.draw() # plota o background

            self.player.update((self.movement [3] - self.movement[2], self.movement[1] - self.movement[0]))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
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

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()