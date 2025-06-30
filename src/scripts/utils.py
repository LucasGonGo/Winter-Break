import pygame

BASE_IMG_PATH = 'assets/images/'

def load_image(path):
    img = pygame.load_image(BASE_IMG_PATH + path).convert()
    img.set_colorkey('black')
    return img