from weapons.weapon import Weapon
class GenesisForge(Weapon):
  def __init__(self):
      super().__init__("Genesis Forge", damage=0, cooldown=5.0)

  def use(self):
      print(f"{self.name} channels celestial energy into creation.")
      print("Particles swirl as new forms are forged from light.")