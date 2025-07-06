from weapons.weapon import Weapon

class VoltEdgeBlades(Weapon):
  def __init__(self):
    super().__init__("Volt Edge Blades", damage=50, cooldown=1.8)
    def use(self):
      print(f"{self.name} slice forward with lightning precision.")
      print("Electric sparks leave jagged trails.")