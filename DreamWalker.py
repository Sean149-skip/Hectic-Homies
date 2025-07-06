class DreamWalker:
  def __init__(self): self.name = "Dream Walker"
  def activate(self, user, target): 
    user.floating = True
    user.collision_damage = True