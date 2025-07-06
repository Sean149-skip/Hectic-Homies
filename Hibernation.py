class Hibernation:
  def __init__(self): self.name = "Hibernation"
  def activate(self, user, target): 
    user.sleeping = True 
    target.touch_damage = 30