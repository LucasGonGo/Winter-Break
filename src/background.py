import pygame

from scripts.utils import load_image

class Background:
    def __init__(self, screen):
        self.screen = screen

        img = load_image('background/test.png')

        self.image = pygame.transform.smoothscale(img, (362, 272))

        self.rect = self.image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))


    def draw(self):
        self.screen.blit(self.image, self.rect.topleft)

    def update(self):
        # pra fazer animaçãozinha de fundo gay
        pass

    def get_rect(self):
        return self.rect