from weapons.weapon import Weapon
class HooperGauntlets(Weapon):
  def __init__(self):
      super().__init__("Hooper Gauntlets", damage=35, cooldown=1.5)

  def use(self):
      print(f"{self.name} slam with court energy.")
      print("Shockwave resembles basketball net pattern.")