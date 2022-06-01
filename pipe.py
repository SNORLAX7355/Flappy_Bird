import pygame
from pygame.sprite import Sprite

class Pipe(Sprite):
    """Class to represent singular pipe"""

    def __init__(self, ai_game):
        """Initialize the pipes and set position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load pipe image and set rect
        self.image = pygame.image.load('images\Pipe.bmp')
        self.rect = self.image.get_rect()

        #store pipes's exact location
        self.rect.x = 540
        self.x = float(self.rect.x)

        #pipe y coordinates
        self.pipe_height = [-690, -607.5, -525, -422.5, -360, -277.5, -195]

    def update(self, dt):
        """Move pipes left across the screen"""
        self.x -= self.settings.pipe_speed * dt
        self.rect.x = self.x