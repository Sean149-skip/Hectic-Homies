class SwordOfHydration(Weapon):
    def __init__(self):
        super().__init__("Sword of Hydration", damage=36, cooldown=2.1)

    def use(self):
        print("Cleanses and strikes with tidal bursts.")
