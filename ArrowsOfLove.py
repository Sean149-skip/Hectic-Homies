class ArrowsOfLove:
  def __init__(self): self.name = "Arrows of Love"
  def activate(self, user, target): target.linked_to = user.last_target
