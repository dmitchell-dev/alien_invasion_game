class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion in an active state
        self.game_active = False

        # High score should never be reset
        with open(self.settings.filename) as file_object:
            contents = int(file_object.read())
        self.high_score = contents

    def reset_stats(self):
        """Initialise stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1