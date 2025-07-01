import pygame

BASE_IMG_PATH = 'assets/images/'

def load_image(path, scale=None):
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    if scale:
        img = pygame.transform.scale(img, scale)
    return img