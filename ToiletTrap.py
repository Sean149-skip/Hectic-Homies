class ToiletTrap:
  def __init__(self): self.name = "Toilet Trap"
  def activate(self, user, target): target.snared = True