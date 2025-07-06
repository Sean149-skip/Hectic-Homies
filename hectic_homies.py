character_data = {
    "The Hydrator": {
        "weapon": "Sword of Hydration",
        "abilities": {
            "Hydration": {"type": "buff", "effect": "damage", "value": 1.5, "description": "Buffs user, increasing damage"},
            "Glass or Gas": {"type": "random", "options": [
                {"type": "buff", "effect": "speed", "value": 1.5},
                {"type": "damage", "value": 10}
            ], "description": "50% speed buff or poison cloud"},
            "SohCahToa": {"type": "snare", "damage": 15, "description": "Creates a triangle trap"},
            "Straw Swan": {"type": "damage", "value": 20, "description": "Pecking swan attack"}
        }
    },
    "The Brain Rotter": {
        "weapon": "Minwarp Staff",
        "abilities": {
            "Toilet Trap": {"type": "trap", "damage": 15, "description": "Trap deals damage on contact"},
            "Falc Tuah": {"type": "damage", "value": 20, "description": "Falcon projectile"},
            "The Fade": {"type": "invisibility", "duration": 2, "description": "Become invisible for 2 turns"},
            "5 Big Booms": {"type": "multi_explode", "explosions": 5, "chance": 0.2, "damage": 5, "description": "Random explosions"}
        }
    }
}
import random

class Player:
    def __init__(self, name, character):
        self.name = name
        self.character = character
        self.health = 100
        self.damage_buff = 1.0
        self.speed_buff = 1.0
        self.resistance = 1.0
        self.invisible_turns = 0

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        actual_damage = int(amount * self.resistance)
        self.health = max(0, self.health - actual_damage)
        print(f"{self.name} takes {actual_damage} damage! Health is now {self.health}.")

    def heal(self, amount):
        self.health = min(100, self.health + amount)
        print(f"{self.name} heals for {amount}. Health is now {self.health}.")

    def use_ability(self, ability_name, opponent):
        ability = character_data[self.character]["abilities"][ability_name]
        print(f"{self.name} uses {ability_name}: {ability['description']}")
        if ability["type"] == "buff":
            if ability["effect"] == "damage":
                self.damage_buff = ability["value"]
            elif ability["effect"] == "speed":
                self.speed_buff = ability["value"]
        elif ability["type"] == "random":
            outcome = random.choice(ability["options"])
            if outcome["type"] == "buff":
                self.speed_buff = outcome["value"]
            elif outcome["type"] == "damage":
                opponent.take_damage(outcome["value"])
        elif ability["type"] == "damage":
            opponent.take_damage(ability["value"])
        elif ability["type"] == "snare":
            opponent.take_damage(ability["damage"])
        elif ability["type"] == "trap":
            opponent.take_damage(ability["damage"])
        elif ability["type"] == "invisibility":
            self.invisible_turns = ability["duration"]
        elif ability["type"] == "multi_explode":
            for _ in range(ability["explosions"]):
                if random.random() < ability["chance"]:
                    opponent.take_damage(ability["damage"])
def list_characters():
    print("\nAvailable Characters:")
    for name in character_data:
        print(f" - {name}")

def select_character():
    list_characters()
    while True:
        choice = input("Choose your character: ").strip()
        if choice in character_data:
            print(f"\n{choice} selected.")
            print(f"Weapon: {character_data[choice]['weapon']}")
            print("Abilities:")
            for ability, data in character_data[choice]["abilities"].items():
                print(f"  - {ability}: {data['description']}")
            return choice
        else:
            print("Invalid character. Please try again.")

def choose_ability(player):
    abilities = character_data[player.character]["abilities"]
    print(f"\n{player.name}'s turn. Choose an ability:")
    for i, ability in enumerate(abilities.keys(), 1):
        print(f"{i}. {ability} - {abilities[ability]['description']}")
    while True:
        choice = input("Enter ability number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(abilities):
            return list(abilities.keys())[int(choice) - 1]
        else:
            print("Invalid input. Try again.")

def play_game():
    print("🎮 Welcome to Hectic Homies Battle Game!")
    human_name = input("Enter your name: ")
    human_char = select_character()
    comp_char = random.choice(list(character_data.keys()))
    print(f"\nComputer has selected: {comp_char}")
    human = Player(human_name, human_char)
    computer = Player("Computer", comp_char)
    round_num = 1
    while human.is_alive() and computer.is_alive():
        print(f"\n--- Round {round_num} ---")
        ability_name = choose_ability(human)
        human.use_ability(ability_name, computer)
        if not computer.is_alive():
            break
        comp_ability = random.choice(list(character_data[computer.character]["abilities"].keys()))
        print(f"\nComputer's turn.")
        computer.use_ability(comp_ability, human)
        round_num += 1
    if human.is_alive():
        print(f"\n🎉 {human.name} wins!")
    else:
        print("\n💀 Computer wins!")

# Start the game
play_game()
