import pygame
from pygame.sprite import Sprite

class BottomHitbox(Sprite):
    """class for top hitbox"""

    def __init__(self, ai_game):
        """Initialize all properties of pipe hitbox"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #set up hitboxes
        self.hitbox = pygame.Surface([76, 744], pygame.SRCALPHA)
        self.rect = self.hitbox.get_rect()

        #store hitbox exact location
        self.rect.x = 540
        self.x = float(self.rect.x)

    def update(self):
        """Move hitbox with the pipes"""
        self.x -= self.settings.pipe_speed
        self.rect.x = self.x