class VolatileDefense:
  def __init__(self): self.name = "Volatile Defense"
  def activate(self, user, target): 
    if target.attacking: 
      target.exploded = True