class StrawSwanStrike:
    def __init__(self):
        self.name = "Straw Swan"
    def activate(self, user, target):
        target.latched = True
        target.peck_damage = 5  # placeholder effect
