class SeathString(Weapon):
    def __init__(self):
        super().__init__("Death String", damage=42, cooldown=1.3)

    def use(self):
        print("Spins with rapid multi-hit lash and wild speed.")
