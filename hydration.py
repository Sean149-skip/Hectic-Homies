class HydrationBuff:
  def __init__(self):
      self.name = "Hydration"
  def activate(self, user, target):
      user.damage_boost = True