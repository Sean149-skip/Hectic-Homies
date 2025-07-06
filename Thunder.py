class Thunder:
  def __init__(self): self.name = "Thunder"
  def activate(self, user, target): target.poisoned = True; target.exploded = True