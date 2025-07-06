class RegalScepter(Weapon):
    def __init__(self):
        super().__init__("Regal Scepter", damage=37, cooldown=1.6)

    def use(self):
        print("Strikes low and fast — compact but punishing.")
