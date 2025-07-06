class CommandersRally:
  def __init__(self):
      self.cooldown = 300
      self.timer = 0

  def execute(self, user, allies):
      if self.timer == 0:
          for ally in allies:
              ally.speed_boost = 2
              ally.damage_buff = True
          self.timer = self.cooldown

  def update(self):
      if self.timer > 0:
          self.timer -= 1
