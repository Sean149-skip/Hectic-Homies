class ShrinkRay:
  def __init__(self): self.name = "Shrink"
  def activate(self, user, target): 
    target.size = "tiny"  
    target.damage_taken *= 1.5

