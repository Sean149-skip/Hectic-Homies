import pygame

class RebirthPulse:
    def __init__(self):
        self.used = False

    def execute(self, user, targets):
        if not self.used:
            self.used = True
            user.health = min(user.health + 25, 100)
            print(f"{user.name} used Rebirth Pulse and healed 25 HP!")

    def update(self, user):
        pass  # one-time use, nothing to update
