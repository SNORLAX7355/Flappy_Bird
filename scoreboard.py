import pygame.font
from pygame.sprite import Group

class Scoreboard:
    """class to report score"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn score into a rendered image"""
        score_str = str(f"Score: {'{:,}'.format(self.stats.score)}")
        self.score_image = self.font.render(score_str, True,
                            self.text_color, None)
        
        #coordinates for score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn high score into a rendered image"""
        high_score_str = str(f"High Score: {'{:}'.format(self.stats.high_score)}")
        self.high_score_image = self.font.render(high_score_str, True, 
                                                    self.text_color, None)

        #coordinates for high score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.centerx + 20
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score and high score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_scores(self):
        """Check if there's new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()