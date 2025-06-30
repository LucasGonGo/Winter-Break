import pygame

from scripts.utils import load_image

class Background:
    def __init__(self, screen):
        self.screen = screen
        self.background = load_image('assets/images/test.png')
        bg_rect = self.background.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.bg_pos = bg_rect.topleft

    def draw(self):
        self.screen.blit(self.background, self.bg_pos)

    def update(self):
        # pra fazer animaçãozinha de fundo gay
        pass