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

        min_x = bg_rect.left
        max_x = bg_rect.right - self.size[0]
        min_y = bg_rect.top
        max_y = bg_rect.bottom - self.size[1]

        self.pos[0] = max(min_x, min(new_x, max_x))
        self.pos[1] = max(min_y, min(new_y, max_y))

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)