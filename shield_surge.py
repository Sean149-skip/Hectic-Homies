import pygame

class ShieldSurge:
    def __init__(self):
        self.duration = 3000  # milliseconds
        self.cooldown = 7000
        self.last_used = -9999
        self.active_until = 0

    def execute(self, user, targets):
        now = pygame.time.get_ticks()
        if now - self.last_used >= self.cooldown:
            self.last_used = now
            self.active_until = now + self.duration
            user.shielded = True
            print(f"{user.name} activated Shield Surge!")

    def update(self, user):
        if pygame.time.get_ticks() > self.active_until:
            user.shielded = False
