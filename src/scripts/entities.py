import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos) # mais facil de trabalhar com listas
        self.size = size
        self.velocity = [10, 10] 

    def update(self, movement=(0,0)):
        frame_movement = (movement[0] * self.velocity[0], movement[1] * self.velocity[1])

        new_x = self.pos[0] + frame_movement[0]
        new_y = self.pos[1] + frame_movement[1]
        
        bg_rect = self.game.background.get_rect()

        half_width = self.size[0] // 2
        half_height = self.size[1] // 2

        min_x = bg_rect.left + half_width
        max_x = bg_rect.right - half_width
        min_y = bg_rect.top + half_height
        max_y = bg_rect.bottom - half_height

        self.pos[0] = max(min_x, min(new_x, max_x))
        self.pos[1] = max(min_y, min(new_y, max_y))

    def render(self, surf):
        image = self.game.assets[self.type]
        rect = image.get_rect(center=(int(self.pos[0]), int(self.pos[1])))
        surf.blit(image, rect)