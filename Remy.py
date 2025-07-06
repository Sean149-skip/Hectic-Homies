class Remy:
  def __init__(self): self.name = "Remy"
  def activate(self, user, target): 
    target.distracted = True 
    target.damage_over_time = True