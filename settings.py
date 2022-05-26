class Settings:
    """Stores all settings for Flappy Bird"""

    def __init__(self):
        """Initialize game settings"""
        #screen settings
        self.screen_width = 540
        self.screen_height = 812
        self.bg_color = (134, 206, 235)
        
        self.pipes_allowed = 3
        self.pipe_sd_incr = 1.25
        self.timer_sd_incr = 1.025

        self.changing_stats()
    
    def changing_stats(self):
        """Initialize stats that change over time"""
        self.timer = 1.6
        self.pipe_speed = 200

    def increase_speed(self):
        """Increase speed of changing stats"""
        if self.timer < 1.7:
            self.timer *= self.timer_sd_incr
        self.pipe_speed *= self.pipe_sd_incr
