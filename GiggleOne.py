class GiggleOne:
  def __init__(self): self.name = "Giggle One"
  def activate(self, user, target): target.stunned = True if target.attacking else False