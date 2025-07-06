from weapons.weapon import Weapon
class GridironGauntlet(Weapon):
  def __init__(self):
      super().__init__("Gridiron Gauntlet", damage=55, cooldown=2.3)

  def use(self):
      print(f"{self.name} charges forward with brute-force punch.")
      print("Yard-marker energy trails streak behind impact.")