from weapons.weapon import Weapon

class BreezeBlaster(Weapon):
    def __init__(self):
        super().__init__("Breeze Blaster", damage=40, cooldown=2.2)

    def use(self):
        print(f"{self.name} fires concentrated blast of air.")
        print("Wind vortex spirals forward with high pressure.")