import pygame

class MasterpieceOfDestruction:
    def __init__(self):
        self.cooldown = 10000  # 10 seconds cooldown
        self.last_used = -9999

    def execute(self, user, targets):
        now = pygame.time.get_ticks()
        if now - self.last_used >= self.cooldown:
            self.last_used = now
            print(f"{user.name} unleashes a Masterpiece of Destruction!")
            for target in targets:
                # Larger hitbox range to feel like a blast
                if user.rect.colliderect(target.rect.inflate(80, 80)):
                    damage = 30 + user.damage_bonus
                    knockback = -40 if user.flip else 40
                    target.health -= damage
                    target.rect.x += knockback
                    print(f"{target.name} is rocked by creative chaos! Took {damage} damage and was knocked back.")

    def update(self, user):
        pass  # Optional: charge timer visuals or sound cues
