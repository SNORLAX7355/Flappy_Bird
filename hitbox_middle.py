import pygame
from pygame.sprite import Sprite

class MiddleHitbox(Sprite):
    """class for middle hitbox"""

    def __init__(self, ai_game):
        """Initialize all properties of pipe hitbox"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #set up hitboxes
        self.hitbox = pygame.Surface([10, 211], pygame.SRCALPHA)
        self.rect = self.hitbox.get_rect()

        #store hitbox exact location
        self.rect.x = 578
        self.x = float(self.rect.x)

    def update(self, dt):
        """Move hitbox with the pipes"""
        self.x -= self.settings.pipe_speed * dt
        self.rect.x = self.x