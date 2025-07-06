class ArtisticExpression:
  def __init__(self):
    self.cooldown = 400
    self.timer = 0
def execute(self, user, target):
  if self.timer == 0:
    target.health -= 20
    target.hit = True
    self.timer = self.cooldown
def update(self):
  if self.timer > 0:
    self.timer -= 1
