class GiggleTwo:
  def __init__(self): self.name = "Giggle Two"
  def activate(self, user, target): target.stunned = True if target.attacking else False