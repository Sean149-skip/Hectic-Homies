import pygame

class InspireAllies:
    def __init__(self):
        self.cooldown = 8000
        self.last_used = -9999
        self.clones = []

    def execute(self, user, targets):
        now = pygame.time.get_ticks()
        if now - self.last_used >= self.cooldown and len(self.clones) < 2:    
            pass 