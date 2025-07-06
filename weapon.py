class Weapon:
    def __init__(self, name, damage, cooldown):
        self.name = name
        self.damage = damage
        self.cooldown = cooldown

    def use(self):
        print(f"{self.name} activated! Deals {self.damage} damage.")