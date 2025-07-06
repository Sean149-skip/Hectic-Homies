class PickleBreadBuff:
  def __init__(self): self.name = "Pickle Bread"
  def activate(self, user, target): 
    user.damage_boost = True 
    user.speed_boost = True