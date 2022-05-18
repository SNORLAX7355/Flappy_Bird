class GameStats:
    """Track stats for Flappy Bird"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change"""
        self.update_score = 1
        self.score = 0