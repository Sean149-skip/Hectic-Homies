class RudeAwakening:
  def __init__(self): self.name = "Rude Awakening"
  def activate(self, user, target): 
    if target.attacking: 
      target.launched = True