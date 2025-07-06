class ALilJig:
  def __init__(self): self.name = "A Lil Jig"
  def activate(self, user, target): 
    target.dancing = True 
    target.stunned = True