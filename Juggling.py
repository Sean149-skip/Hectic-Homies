class Juggling:
  def __init__(self): self.name = "Juggling"
  def activate(self, user, target): 
    target.launched = True 
    target.spinning = True