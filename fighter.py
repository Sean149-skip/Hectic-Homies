import pygame

class Fighter:
    def __init__(self, x, y, name, flip, player, abilities, weapon=None, sprite=None):
        self.rect = pygame.Rect(x, y, 80, 100)
        self.name = name
        self.flip = flip
        self.player = player
        self.abilities = abilities
        self.weapon = weapon
        self.sprite = sprite if sprite else pygame.Surface((80, 100))

        # Core stats
        self.health = 100
        self.attacking = False
        self.attack_cooldown = 0
        self.hit = False
        self.shielded = False
        self.damage_bonus = 0
        self.damage_reduction = 1.0
        self.weapon_type = "melee"  # "ranged" supported
        self.stunned_until = 0
        self.combo_tracker = None  # hook this externally if needed

    def move(self, target):
        if pygame.time.get_ticks() < self.stunned_until:
            return  # stunned

        keys = pygame.key.get_pressed()

        if self.player == 1:
            if keys[pygame.K_a]: 
                self.rect.x -= 5
            if keys[pygame.K_d]: 
                self.rect.x += 5
            if keys[pygame.K_f] and "F" in self.abilities:
                self.execute_ability("F", target)
            if keys[pygame.K_g] and "G" in self.abilities:
                self.execute_ability("G", self)
            if keys[pygame.K_k] and "K" in self.abilities:
                self.execute_ability("K", target)
            if keys[pygame.K_l] and "L" in self.abilities:
                self.execute_ability("L", self)

        elif self.player == 2:
            if keys[pygame.K_LEFT]: 
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]: 
                self.rect.x += 5
            if keys[pygame.K_KP1] and "F" in self.abilities:
                self.execute_ability("F", target)
            if keys[pygame.K_KP2] and "G" in self.abilities:
                self.execute_ability("G", self)
            if keys[pygame.K_KP3] and "K" in self.abilities:
                self.execute_ability("K", target)
            if keys[pygame.K_KP_ENTER] and "L" in self.abilities:
                self.execute_ability("L", self)

    def execute_ability(self, key, target):
        ability = self.abilities.get(key)
        if ability:
            damage = ability.execute(self, [target])
            if damage and hasattr(target, "rect"):
                target.take_damage(damage)
                if self.combo_tracker:
                    self.combo_tracker.register_hit(damage, target.rect.centerx, target.rect.y)

    def update(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # Passive effects
        self.damage_reduction = 0.85 if self.name == "Iron Commander" and self.health <= 40 else 1.0
        self.damage_bonus = 1 if self.name == "The Creator" and self.health <= 25 else 0

        # Ability passive loops
        for ability in self.abilities.values():
            if hasattr(ability, "update"):
                ability.update(self)

        if self.weapon and hasattr(self.weapon, "update"):
            self.weapon.update(self)

    def draw(self, surface):
        # Visual
        if self.sprite:
            surface.blit(pygame.transform.flip(self.sprite, self.flip, False), self.rect)
        else:
            color = (0, 200, 255) if not self.shielded else (0, 100, 255)
            pygame.draw.rect(surface, color, self.rect)

        # Optional weapon visuals
        if self.weapon and hasattr(self.weapon, "draw"):
            self.weapon.draw(surface, self.rect.center, flip=self.flip)

        # UI
        font = pygame.font.Font(None, 24)
        surface.blit(font.render(self.name, True, (255, 255, 255)), (self.rect.x, self.rect.y - 25))
        pygame.draw.rect(surface, (0, 255, 0), (self.rect.x, self.rect.y - 10, self.health * 0.8, 5))

    def take_damage(self, amount):
        if self.shielded:
            print(f"{self.name} blocked the damage!")
            return
        adjusted = int(amount * self.damage_reduction)
        self.health = max(self.health - adjusted, 0)
        print(f"{self.name} took {adjusted} damage!")

    def basic_attack(self, target):
        if self.weapon_type == "melee":
            if self.rect.colliderect(target.rect):
                damage = 5 + self.damage_bonus
                target.take_damage(damage)
                if self.combo_tracker:
                    self.combo_tracker.register_hit(damage, target.rect.centerx, target.rect.y)
        elif self.weapon_type == "ranged":
            self.shoot_projectile(target)

    def shoot_projectile(self, target):
        # ⚡ Optional: spawn projectile object here
        print(f"{self.name} shoots a projectile at {target.name}!")

      
