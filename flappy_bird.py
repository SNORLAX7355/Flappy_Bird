import sys
from time import sleep
import pygame
import random

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from bird import Bird
from pipe import Pipe
from hitbox_top import TopHitbox
from hitbox_middle import MiddleHitbox
from hitbox_bottom import BottomHitbox
from start_button import Button

# add items (bonus points, slow down, etc)
class FlappyBird:
    """Overall class to manage the game"""
    
    def __init__(self):
        """Initialize game & create resources"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Flappy Bird")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.bird = Bird(self)

        #pipes
        self.pipes = pygame.sprite.Group()
        self.timer = self.settings.timer + 1.4
        self.pipe_y = 2
        self.multiplier = [-1, 1]
        self.count = 0
        self.speedup = 10
        self.sdlvl = 0
        self.score_dvd = 20

        #This initializes the hitboxes
        self.th = pygame.sprite.Group()
        self.bh = pygame.sprite.Group()
        self.mh = pygame.sprite.Group()

        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start main loop for game"""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.bird.update(self.dt)
                self._update_pipes()
                self._update_hitbox()
                self.timer -= self.dt
                if self.timer <= 0:
                    self._create_pipe()
                    self.timer = self.settings.timer

            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_play_button(self, mouse_pos):
        """reset game then start new game if clicked"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.changing_stats()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.bird.reset_bird()
            self.pipes.empty()
            self.timer = 3
            self.pipe_y = 2
            self.speedup = 10
            self.sdlvl = 0
            self.score_dvd = 20
            self.th.empty()
            self.mh.empty()
            self.bh.empty()
            pygame.mouse.set_visible(False)
            sleep(0.5)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.bird.a += 1
            self.bird.jump = True

    def _create_pipe(self):
        """Create pipes w/ hitboxes"""
        if len(self.pipes) < self.settings.pipes_allowed:
            self.count = 0
            while self.count != 1:
                pipe = Pipe(self)
                top_h = TopHitbox(self)
                middle_h = MiddleHitbox(self)
                bottom_h = BottomHitbox(self) 
                num = random.randint(1,3)
                direction = random.choice(self.multiplier)
                self.pipe_y += num * direction
                
                if self.pipe_y >= 0 and self.pipe_y < 7:
                    pipe.rect.y = pipe.pipe_height[self.pipe_y]
                    top_h.rect.y = pipe.pipe_height[self.pipe_y]
                    middle_h.rect.y = pipe.pipe_height[self.pipe_y] + 744
                    bottom_h.rect.y = pipe.pipe_height[self.pipe_y] + 955
                    self.pipes.add(pipe)
                    self.th.add(top_h)
                    self.mh.add(middle_h)
                    self.bh.add(bottom_h)
                    self.count = 1
                else:
                    self.pipe_y -= num * direction
    
    def _update_pipes(self):
        """update pipe positionn and get rid of old ones"""
        self.pipes.update(self.dt)

        for pipe in self.pipes.copy():
            if pipe.rect.right <= 0:
                self.pipes.remove(pipe)

        if self.stats.score % 10 == 5 and self.timer <= .04:
            self.speedup = 0
            self.sdlvl = 1
            print("Changed")
        if self.stats.score % 10 == self.speedup and self.sdlvl == 1:
            self.sdlvl = 0
            self.settings.increase_speed()
            print(f"Change: (Score: {self.stats.score}) (Timer: {self.settings.timer}) (pipe speed: {self.settings.pipe_speed})")

    def _update_hitbox(self):
        """update hitbox for pipe"""
        self.th.update(self.dt)
        self.mh.update(self.dt)
        self.bh.update(self.dt)

        for hitbox in self.th.copy():
            if hitbox.rect.right <= 0:
                self.th.remove(hitbox)
        
        for hitbox in self.bh.copy():
            if hitbox.rect.right <= 0:
                self.bh.remove(hitbox)

        if pygame.sprite.spritecollideany(self.bird, self.mh):
            self.stats.score += 1
            self.sb.prep_score()
            self.sb.check_high_scores()
            for hitbox in self.mh.copy():
                if hitbox.rect.left < 160:
                    self.mh.remove(hitbox)

        if pygame.sprite.spritecollideany(self.bird, self.th):
            self._bird_hit()

        if pygame.sprite.spritecollideany(self.bird, self.bh):
            self._bird_hit()

    def _bird_hit(self):
        """Respond to bird collision"""
        self.stats.game_active = False
        pygame.mouse.set_visible(True)

    def _update_screen(self):
        """update imgaes on screen"""
        self.screen.fill(self.settings.bg_color)

        self.dt = self.clock.tick(30) / 1000

        self.bird.blitme()
        self.pipes.draw(self.screen)  

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    #make game instance, run game
    ai = FlappyBird()
    ai.run_game()