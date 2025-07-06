class CounterAbsorb:
  def __init__(self): self.name = "Counter Absorb"
  def activate(self, user, target): 
    if target.attacking: 
      target.damage_reflected = True