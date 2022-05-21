class Settings:
    """Stores all settings for Flappy Bird"""

    def __init__(self):
        """Initialize game settings"""
        #screen settings
        self.screen_width = 540
        self.screen_height = 812
        self.bg_color = (134, 206, 235)
        
        self.pipe_speed = 200
        self.pipes_allowed = 3