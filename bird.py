import pygame

class Bird:
    """class for the flying bird"""

    def __init__(self, ai_game):
        """Initialize bird and its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load image of bird
        self.image = pygame.image.load('C:\Python Coding\Flappy_Bird\images\Bird.bmp')
        self.rect = self.image.get_rect()

        #start position
        self.rect.x = 100
        self.rect.y = 250

        self.y = float(self.rect.y)

        #movement flag
        self.jump = False
        self.a = 0
        self.b = 0
        self.v, self.v2 = 8, 8
        self.fv = 1

    def update(self):
        """Update bird position"""
        if self.jump and self.rect.top > 0 and (self.a % 2 == 0):
            F = (1/2) * (self.v**2)
            self.y -= F
            self.v -= 1

            self.b = 0
            self.v2 = 8

            if self.v == 0:
                self.jump = False
                self.fv = 1
                self.v = 8
                self.a = 0

        if self.jump and self.rect.top > 0 and (self.a % 2 == 1):
            F = (1/2) * (self.v2**2)
            self.y -= F
            self.v2 -= 1

            self.b = 0
            self.v = 8
            
            if self.v2 == 0:
                self.jump = False
                self.fv = 1
                self.v2 = 8
                self.a = 0

        if self.rect.top < 0:
            self.fv = 1
            self.y = 1
            self.jump = False

        if not self.jump and self.rect.bottom < self.screen_rect.bottom and self.b == 0:
            Y = (1/2) * (self.fv**2)
            self.y += Y
            self.fv += .5
        
        if self.rect.bottom > self.screen_rect.bottom:
            self.y = 764
            self.b = 1
        
        self.rect.y = self.y

    def reset_bird(self):
        """reset bird starting position"""
        self.rect.y = 250
        self.y = self.rect.y
        self.jump = False
        self.a = 0
        self.v, self.v2 = 8, 8
        self.fv = 1

    def blitme(self):
        """Draw bird at its current location"""
        self.screen.blit(self.image, self.rect)