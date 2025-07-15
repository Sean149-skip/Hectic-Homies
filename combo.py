import pygame

class DamagePopup:
    def __init__(self, x, y, damage):
        self.x = x
        self.y = y
        self.damage = damage
        self.alpha = 255
        self.timer = 60  # lasts for 1 second at 60 FPS
        self.font = pygame.font.Font(None, 30)

    def update(self):
        self.y -= 1
        self.alpha -= 4
        self.timer -= 1

    def draw(self, surface):
        if self.timer > 0:
            text = self.font.render(f"{self.damage}", True, (255, 255, 0))
            text.set_alpha(max(self.alpha, 0))
            surface.blit(text, (self.x, self.y))

class ComboTracker:
    def __init__(self):
        self.hit_count = 0
        self.total_damage = 0
        self.combo_timer = 120  # 2 seconds to keep combo alive
        self.active = False
        self.popups = []

    def register_hit(self, damage, x, y):
        self.hit_count += 1
        self.total_damage += damage
        self.combo_timer = 120
        self.active = True
        self.popups.append(DamagePopup(x, y, damage))

    def update(self):
        if self.combo_timer > 0 and self.active:
            self.combo_timer -= 1
        elif self.active:
            self.reset()

        for popup in self.popups:
            popup.update()
        self.popups = [p for p in self.popups if p.timer > 0]

    def draw(self, surface):
        font = pygame.font.Font(None, 40)
        if self.active:
            combo_text = font.render(f"{self.hit_count} Hit Combo!", True, (255, 80, 80))
            damage_text = font.render(f"Total Damage: {self.total_damage}", True, (255, 255, 255))
            surface.blit(combo_text, (WIDTH // 2 - 100, 60))
            surface.blit(damage_text, (WIDTH // 2 - 100, 100))

        for popup in self.popups:
            popup.draw(surface)

    def reset(self):
        self.hit_count = 0
        self.total_damage = 0
        self.active = False
        self.popups.clear()
