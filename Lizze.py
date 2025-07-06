class Lizze:
  def __init__(self): self.name = "Lizze"
  def activate(self, user, target): 
    user.transformed = "lizard" 
    user.speed_boost = True