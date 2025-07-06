class MindWarpStaff(Weapon):
    def __init__(self):
        super().__init__("Mindwarp Staff", damage=33, cooldown=2.2)

    def use(self):
        print("Emits psychic pulses that disorient and confuse.")
