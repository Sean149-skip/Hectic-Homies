from weapons.weapon import Weapon
class ChuckleChucks(Weapon):
  def __init__(self):
      super().__init__("Chuckle Chucks", damage=30, cooldown=1.2)

  def use(self):
      print(f"{self.name} thrown in chaotic arc.")
      print("Distorts air with warped visual ripple.")