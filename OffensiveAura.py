class OffensiveAura:
  def __init__(self): self.name = "Offensive Aura"
  def activate(self, user, target): 
    if target.nearby: 
      target.damage_over_time = True