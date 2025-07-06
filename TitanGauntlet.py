from weapons.weapon import Weapon

class CommanderGauntlet(Weapon):
    def __init__(self):
        super().__init__("Titan Gauntlet", damage=65, cooldown=2.8)

    def use(self):
        print(f"{self.name} unleashes kinetic blast!")
        print("Shockwave rips through battlefield with warped air and rubble.")