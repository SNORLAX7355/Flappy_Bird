import pygame
from pygame.sprite import Sprite

class Coin(Sprite):
    """Class to represent bonus coins"""

    def __init__(self, ai_game):
        """Initialize the coin and set position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load coin images and get rect
        self.image = pygame.image.load('images\coin.bmp')
        self.rect = self.image.get_rect()

        #store coin's exact location
        self.rect.x = 552
        self.x = float(self.rect.x)

    def update(self, dt):
        """Move coin left across the screen"""
        self.x -= self.settings.pipe_speed * dt
        self.rect.x = self.x