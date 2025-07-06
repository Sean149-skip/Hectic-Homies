class CrownTheft:
  def __init__(self): self.name = "Crown Theft"
  def activate(self, user, target): user.stolen_ability = target.last_used_ability