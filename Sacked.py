class Sacked:
  def __init__(self): self.name = "Sacked"
  def activate(self, user, target): target.stunned = True