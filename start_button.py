import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set dimension and properties for the button
        self.width, self.height = 100, 50
        self.button_color = (204, 153, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #build button's rect object and center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #prep button message
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into rendered image and center text"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw blank button then message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)