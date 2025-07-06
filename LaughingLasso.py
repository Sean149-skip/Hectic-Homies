from weapons.weapon import Weapon
class LaughingLasso(Weapon):
  def __init__(self):
      super().__init__("Laughing Lasso", damage=15, cooldown=3.5)

  def use(self):
      print(f"{self.name} lashes out and restrains the target.")
      print("Emits oscillating hum and pulls tight before snapping back.")