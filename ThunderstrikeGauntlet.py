from weapons.weapon import Weapon
class ThunderstrikeGauntlet(Weapon):
  def __init__(self):
      super().__init__("Thunderstrike Gauntlet", damage=60, cooldown=2.5)

  def use(self):
      print(f"{self.name} slams forward with thunder force.")
      print("Electric arcs dance as shockwaves burst outward.")