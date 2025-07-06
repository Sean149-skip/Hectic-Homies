class LightningStrike:
  def __init__(self): self.name = "Lightning Strike"
  def activate(self, user, target): target.stunned = True