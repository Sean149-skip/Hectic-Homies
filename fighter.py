import pygame

class Fighter:
    def __init__(self, x, y, name, flip, player, abilities):
        self.rect = pygame.Rect(x, y, 80, 100)
        self.name = name
        self.flip = flip
        self.player = player
        self.abilities = abilities
        self.health = 100
        self.attacking = False
        self.attack_cooldown = 0
        self.hit = False
        self.shielded = False
        self.damage_bonus = 0
        self.stunned_until = 0

    def move(self, target):
        keys = pygame.key.get_pressed()

        if self.player == 1:
            if keys[pygame.K_a]: 
                self.rect.x -= 5
            if keys[pygame.K_d]:
                self.rect.x += 5
            if "rally" in self.abilities and keys[pygame.K_q]:
                self.abilities["rally"].execute(self, [self])
            if "shield" in self.abilities and keys[pygame.K_z]:
                self.abilities["shield"].execute(self, [self])
            if "strike" in self.abilities and keys[pygame.K_x]:
                self.abilities["strike"].execute(self, [target])

            
            if keys[pygame.K_LEFT]: 
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]: 
                self.rect.x += 5
            if "artistic" in self.abilities and keys[pygame.K_o]:
                self.abilities["artistic"].execute(self, [target])
            if "rebirth" in self.abilities and keys[pygame.K_k]:
                self.abilities["rebirth"].execute(self, [self])
            if "inspire" in self.abilities and keys[pygame.K_l]:
                self.abilities["inspire"].execute(self, [self])
            if "masterpiece" in self.abilities and keys[pygame.K_SEMICOLON]:
                self.abilities["masterpiece"].execute(self, [target])

    def update(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # Iron Commander Passive
        if self.name == "Iron Commander" and self.health <= 40:
            self.damage_reduction = 0.85
        else:
            self.damage_reduction = 1.0

        # The Creator Passive
        if self.name == "The Creator" and self.health <= 25:
            self.damage_bonus = 1
        else:
            self.damage_bonus = 0

        # Update all abilities
        for ability in self.abilities.values():
            if hasattr(ability, "update"):
                ability.update(self)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 200, 255), self.rect)

    def take_damage(self, amount):
        if not self.shielded:
            adjusted = int(amount * self.damage_reduction)
            self.health -= adjusted
            print(f"{self.name} took {adjusted} damage!")
    
    def basic_attack(self, target):
        if self.weapon_type == "melee":
        # Handle close-range punch, slash, etc.
            if self.rect.colliderect(target.rect):
                target.health -= 5
        elif self.weapon_type == "ranged":
        # Fire small projectile or ranged hitbox            
            shoot_projectile(self, target)    

    def shoot_projectile(attacker, target):
    print(f"{attacker.name} shoots a projectile at {target.name}!")
    
      
