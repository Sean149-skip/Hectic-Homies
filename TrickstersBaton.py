class TrickstersBaton(Weapon):
    def __init__(self):
        super().__init__("Trickster’s Baton", damage=34, cooldown=1.5)

    def use(self):
        print("Unpredictable jabs with distracting sounds.")
