class HeartstringBow(Weapon):
    def __init__(self):
        super().__init__("Heartstring Bow", damage=40, cooldown=1.9)

    def use(self):
        print("Fires sparkling, homing love-tipped arrows.")
