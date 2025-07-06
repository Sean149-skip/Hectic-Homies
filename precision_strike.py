import pygame

class PrecisionStrike:
    def __init__(self):
        self.cooldown = 6000
        self.last_used = -9999

    def execute(self, user, targets):
        now = pygame.time.get_ticks()
        if now - self.last_used >= self.cooldown:
            self.last_used = now
            user.attacking = True
            print(f"{user.name} executes Overclock Strike!")
            for target in targets:
                if user.rect.colliderect(target.rect):
                    target.health -= 25
                    target.hit = True
                    target.rect.x += -30 if user.flip else 30
