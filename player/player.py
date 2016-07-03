from util.history import load_stats


class Player:

    def __init__(self, name, color, health=20, wins=0):
        """Create a new player"""
        self.name = name
        self.color = color
        self.health = health
        self.wins = 0

        try:
            self.wins, self.health = load_stats(self)
        except KeyError:
            pass

    def __repr__(self):
        return self.name

    def reset_health(self):
        """Set player's health to default"""
        self.health = 20

    def health_change(self, change=None):
        """Change player's health by given amount, or reset to default"""
        if not change:
            self.reset_health()
            return

        self.health += change

    def wins_change(self, change):
        """Change player's wins by given amount"""
        if self.wins + change >= 0:
            self.wins += change

