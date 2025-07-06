class PowerNap:
  def __init__(self): self.name = "Power Nap"
  def activate(self, user, target): 
    user.health += 20 
    user.damage_buff = True