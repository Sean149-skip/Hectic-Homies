from weapons.weapon import Weapon 

class BeastmastersWhip(Weapon):
  def __init__(self):
      super().__init__("Beastmaster's Whip", damage=38, cooldown=2.0)

  def use(self):
      print(f"{self.name} lashes out with animalistic force.")
      print("Fangs and feathers trail with tribal energy sparks.")