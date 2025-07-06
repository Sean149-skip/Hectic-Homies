from weapons.weapon import Weapon

class DreamweaverBlade (Weapon):
  def __init__(self):
      super().__init__("Dreamweaver Blade", damage=45, cooldown=2.0)

  def use(self):
        print(f"{self.name} drifts forward with silent arcs.")
        print("Space bends slightly and mist trails behind.")