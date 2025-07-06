import pygame

class TacticalOverwatch:
    def __init__(self):
        self.cooldown = 9000
        self.last_used = -9999
        self.active_until = 0
        self.duration = 5000

    def execute(self, user, targets):
        now = pygame.time.get_ticks()
        if now - self.last_used >= self.cooldown:
            self.last_used = now
            self.active_until = now + self.duration
            print(f"{user.name} activated Tactical Overwatch! Scouting drones deployed.")

            # Buff allies in range
            for ally in targets:
                if user.rect.colliderect(ally.rect.inflate(200, 100)):
                    ally.defense_buff = 0.85  # takes 15% less damage
                    ally.accuracy_buff = True  # logic can be expanded later

    def update(self, user):
        now = pygame.time.get_ticks()
        if now > self.active_until:
            # Remove buffs from all players
            for ally in user.team:
                if hasattr(ally, "defense_buff"):
                    ally.defense_buff = 1.0
                if hasattr(ally, "accuracy_buff"):
                    ally.accuracy_buff = False
