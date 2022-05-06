import pygame

class Bird:
    """class for the flying bird"""

    def __init__(self, ai_game):
        """Initialize bird and its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load image of bird
        self.image = pygame.image.load('Flappy Bird\images\Bird.bmp')
        self.rect = self.image.get_rect()

        #start position
        self.rect.x = 100
        self.rect.y = 250

        self.y = float(self.rect.y)

        #movement flag
        self.jump = False
        self.fall = True
        
    def update(self):
        """Update bird's position based on tap"""
        if self.jump and self.rect.y > 0:
            self.y -= self.settings.bird_speed
        if self.fall and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.bird_speed
        
        self.rect.y = self.y

    def _flight_equation(self, x):
        """equation for the bird's flight"""
        y = -(x-3)**2 + 9
        return y

    def reset_bird(self):
        """reset bird starting position"""
        self.rect.y = 250
        self.y = self.rect.y

    def blitme(self):
        """Draw bird at its current location"""
        self.screen.blit(self.image, self.rect)