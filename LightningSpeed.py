class LightningSpeed:
  def __init__(self): self.name = "Lightning Speed"
  def activate(self, user, target): 
    user.speed_boost = True
    user.jump_boost = True