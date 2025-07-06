import random
class GlassOrGasEffect:
    def __init__(self):
        self.name = "Glass or Gas"
    def activate(self, user, target):
        if random.random() < 0.5:
            user.speed_boost = True
        else:
            target.poisoned = True