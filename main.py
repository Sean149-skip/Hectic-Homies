import pygame
from fighter import Fighter
from combo import ComboTracker  # 💥 Combo counter + damage system
# === Weapon Imports ===
from weapons.BeastmastersWhip import BeastmastersWhip
from weapons.BreezeBlaster import BreezeBlaster
from weapons.ChuckleChucks import ChuckleChucks
from weapons.DeathString import DeathString
from weapons.DreamWeaverBlade import DreamweaverBlade
from weapons.GenesisForge import GenesisForge
from weapons.GridironGauntlet import GridironGauntlet
from weapons.HeartStringBow import HeartstringBow
from weapons.LaughingLasso import LaughingLasso
from weapons.MindwarpStaff import MindWarpStaff
from weapons.RegalScepter import RegalScepter
from weapons.SlamDunkGauntlets import SlamDunkGauntlets
from weapons.SwordOfHydration import SwordOfHydration
from weapons.ThunderstrikeGauntlet import ThunderstrikeGauntlet
from weapons.TitanGauntlet import TitanGauntlet
from weapons.TrickstersBaton import TrickstersBaton
from weapons.VoltEdgeBlades import VoltEdgeBlades

# === Ability Imports ===
from abilities.rally import CommandersRally
from abilities.shield_surge import ShieldSurge
from abilities.precision_strike import PrecisionStrike
from abilities.tactical_overwatch import TacticalOverwatch

from abilities.artistic import ArtisticExpression
from abilities.rebirth_pulse import RebirthPulse
from abilities.inspire_allies import InspireAllies
from abilities.masterpiece import MasterpieceOfDestruction

from abilities.hydration import HydrationBuff
from abilities.glass_or_gas import GlassOrGasEffect
from abilities.sohcahtoa import SohCahToaTrap
from abilities.straw_swan import StrawSwanStrike

from abilities.godspeed import Godspeed
from abilities.picklebreadbuff import PickleBreadBuff
from abilities.Red40Rant import Red40Rant
from abilities.LikeandSubscribe import LikeAndSubscribe

from abilities.crowntheft import CrownTheft
from abilities.shrinkray import ShrinkRay
from abilities.MidgetRage import MidgetRage
from abilities.CounterAbsorb import CounterAbsorb

from abilities.ToiletTrap import ToiletTrap
from abilities.TheFade import TheFade
from abilities.FalcTuah import FalcTuah
from abilities.FiveBigBooms import FiveBigBooms

from abilities.Posterize import Posterize
from abilities.TheSwish import TheSwish
from abilities.AnkleBreaker import AnkleBreaker
from abilities.AboveTheRim import AboveTheRim

from abilities.ArrowsOfLove import ArrowsOfLove
from abilities.Quickfire import Quickfire
from abilities.Flight import Flight
from abilities.CupidsGaze import CupidsGaze

from abilities.TheYapping import TheYapping
from abilities.Juggling import Juggling
from abilities.YouGotJokes import YouGotJokes
from abilities.ALilJig import ALilJig

from abilities.TheEdit import TheEdit
from abilities.TheChillZone import TheChillZone
from abilities.TheMewer import TheMewer
from abilities.RonaldoKick import RonaldoKick

from abilities.Remy import Remy
from abilities.Lizze import Lizze
from abilities.Ellie import Ellie
from abilities.Cornelius import Cornelius

from abilities.LightningStrike import LightningStrike
from abilities.LightningSpeed import LightningSpeed
from abilities.Thunderstrike import Thunderstrike
from abilities.LightningBeforeThunder import LightningBeforeThunder

from abilities.ChaseDown import ChaseDown
from abilities.TheTracker import TheTracker
from abilities.Trucked import Trucked
from abilities.Sacked import Sacked

from abilities.Thunder import Thunder
from abilities.VolatileDefense import VolatileDefense
from abilities.SilentButDeadly import SilentButDeadly
from abilities.OffensiveAura import OffensiveAura

from abilities.Hibernation import Hibernation
from abilities.PowerNap import PowerNap
from abilities.RudeAwakening import RudeAwakening
from abilities.DreamWalker import DreamWalker

from abilities.Giggle import Giggle
from abilities.GiggleOne import GiggleOne
from abilities.GiggleTwo import GiggleTwo
from abilities.Mock import Mock

fighter_1 = None
fighter_2 = None
dummy = None
combo_tracker = None
background = None
game_state = None
winner = None


# === Pygame Initialization ===
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hectic Homies")
clock = pygame.time.Clock()

# === Load Title & Character Images ===
title_bg = pygame.image.load("assets/titlescreen.JPG")
iron_image = pygame.image.load("assets/iron_commander_no_slogan.JPG")
creator_image = pygame.image.load("assets/creator_no_slogan.JPG")
hydrator_image = pygame.image.load("assets/hydrator_no_slogan.JPG")
yoyoer_image = pygame.image.load("assets/yoyoer_no_slogan.JPG")
shortking_image = pygame.image.load("assets/short_king_no_slogan.JPG")
brainrotter_image = pygame.image.load("assets/brain_rotter_no_slogan.JPG")
hooper_image = pygame.image.load("assets/hooper_no_slogan.JPG")
cupid_image = pygame.image.load("assets/cupid_no_slogan.JPG")
jester_image = pygame.image.load("assets/jester_no_slogan.JPG")
chillguy_image = pygame.image.load("assets/chill_guy.JPG")
tamer_image = pygame.image.load("assets/tamer_no_slogan.JPG")
lightning_image = pygame.image.load("assets/lightning_and_thunder_no_slogan.JPG")
shutdown_image = pygame.image.load("assets/shutdown_specialist_no_slogan.JPG")
thunder_image = pygame.image.load("assets/lightning_and_thunder_no_slogan.JPG")
sleeper_image = pygame.image.load("assets/sleeper_no_slogan.JPG")
giggle_image = pygame.image.load("assets/giggle_1_2_no_slogan.JPG")

# === Load Maps ===
map_images = {
    "Citadel Clash": pygame.image.load("Maps/iron_commander_map.JPG"),
    "Creator's Realm": pygame.image.load("Maps/creator_map.JPG"),
    "Sanctuary of Flow": pygame.image.load("Maps/hydrator_map.png"),
    "Cupid's Garden": pygame.image.load("Maps/cupid_map.png"),
    "The Slam Court": pygame.image.load("Maps/hooper_map.png"),
    "Rot Zone": pygame.image.load("Maps/brain_rotter_map.png"),
    "Throne Room": pygame.image.load("Maps/short_king_map.png"),
    "Yo-Yo Arena": pygame.image.load("Maps/yo-yoer_map.png"),
    "Laugh Track Live": pygame.image.load("Maps/jester_map.png"),
    "Chill Zone": pygame.image.load("Maps/chill_guy_map.png"),
    "Wildlands": pygame.image.load("Maps/tamer_map.png"),
    "Voltage Vault": pygame.image.load("Maps/lightning_and_thunder_map.png"),
    "The End Zone": pygame.image.load("Maps/shutdown_specialist_map.png"),
    "Stormfront Arena": pygame.image.load("Maps/lightning_and_thunder_map.png"),
    "Dreamscape": pygame.image.load("Maps/sleeper_map.png"),
    "Clown Tower": pygame.image.load("Maps/giggle_1_and_2_map.png")
}

# === Load Sounds ===
ko_sound = pygame.mixer.Sound("assets/sounds/ko_sound.wav")
pygame.mixer.music.load("assets/sounds/menu_theme.mp3")
pygame.mixer.music.play(-1)

fighter_roster = [
    {
        "name": "Iron Commander",
        "image": iron_image,
        "slogan": "Tactical Might Unleashed.",
        "weapon": TitanGauntlet(),
        "flip": False,
        "abilities": {
            "F": CommandersRally(),
            "G": ShieldSurge(),
            "K": PrecisionStrike(),
            "L": TacticalOverwatch()
        }
    },
    {
        "name": "The Creator",
        "image": creator_image,
        "slogan": "Imagination Meets Power.",
        "weapon": GenesisForge(),
        "flip": False,
        "abilities": {
            "F": ArtisticExpression(),
            "G": RebirthPulse(),
            "K": InspireAllies(),
            "L": MasterpieceOfDestruction()
        }
    },
    {
        "name": "The Hydrator",
        "image": hydrator_image,
        "slogan": "Quench the Chaos.",
        "weapon": SwordOfHydration(),
        "flip": False,
        "abilities": {
            "F": HydrationBuff(),
            "G": GlassOrGasEffect(),
            "K": SohCahToaTrap(),
            "L": StrawSwanStrike()
        }
    },
    {
        "name": "The Yo-Yoer",
        "image": yoyoer_image,
        "slogan": "Spin into action with flavor, speed, and smash!",
        "weapon": DeathString(),
        "flip": False,
        "abilities": {
            "F": Godspeed(),
            "G": PickleBreadBuff(),
            "K": Red40Rant(),
            "L": LikeAndSubscribe()
        }
    },
    {
        "name": "The Short King",
        "image": shortking_image,
        "slogan": "Small stature, mighty impact.",
        "weapon": RegalScepter(),
        "flip": False,
        "abilities": {
            "F": CrownTheft(),
            "G": ShrinkRay(),
            "K": MidgetRage(),
            "L": CounterAbsorb()
        }
    },
    {
        "name": "The Brain Rotter",
        "image": brainrotter_image,
        "slogan": "Flush, pierce, vanish, and explode!",
        "weapon": MindWarpStaff(),
        "flip": False,
        "abilities": {
            "F": ToiletTrap(),
            "G": TheFade(),
            "K": FalcTuah(),
            "L": FiveBigBooms()
        }
    },
    {
        "name": "The Hooper",
        "image": hooper_image,
        "slogan": "Dribble, dunk, and dominate.",
        "weapon": SlamDunkGauntlets(),
        "flip": False,
        "abilities": {
            "F": Posterize(),
            "G": TheSwish(),
            "K": AnkleBreaker(),
            "L": AboveTheRim()
        }
    },
    {
        "name": "Cupid",
        "image": cupid_image,
        "slogan": "Aim for love… striking hearts and uniting souls.",
        "weapon": HeartstringBow(),
        "flip": False,
        "abilities": {
            "F": ArrowsOfLove(),
            "G": Quickfire(),
            "K": Flight(),
            "L": CupidsGaze()
        }
    },
    {
        "name": "The Jester",
        "image": jester_image,
        "slogan": "Chaos is comedy. Comedy is pain.",
        "weapon": TrickstersBaton(),
        "flip": False,
        "abilities": {
            "F": TheYapping(),
            "G": Juggling(),
            "K": YouGotJokes(),
            "L": ALilJig()
        }
    },
    {
        "name": "The Chill Guy",
        "image": chillguy_image,
        "slogan": "Too cool to care. Too dangerous to doubt.",
        "weapon": BreezeBlaster(),
        "flip": False,
        "abilities": {
            "F": TheEdit(),
            "G": TheChillZone(),
            "K": TheMewer(),
            "L": RonaldoKick()
        }
    },
    {
        "name": "The Tamer",
        "image": tamer_image,
        "slogan": "Nature answers to none... except me.",
        "weapon": BeastmastersWhip(),
        "flip": False,
        "abilities": {
            "F": Remy(),
            "G": Lizze(),
            "K": Ellie(),
            "L": Cornelius()
        }
    },
    {
        "name": "The Lightning",
        "image": lightning_image,
        "slogan": "Strike fast. Confuse faster.",
        "weapon": VoltEdgeBlades(),
        "flip": False,
        "abilities": {
            "F": LightningStrike(),
            "G": LightningSpeed(),
            "K": Thunderstrike(),
            "L": LightningBeforeThunder()
        }
    },
    {
        "name": "The Shutdown Specialist",
        "image": shutdown_image,
        "slogan": "Defense wins games. I win all of them.",
        "weapon": GridironGauntlet(),
        "flip": False,
        "abilities": {
            "F": ChaseDown(),
            "G": TheTracker(),
            "K": Trucked(),
            "L": Sacked()
        }
    },
    {
        "name": "The Thunder",
        "image": thunder_image,
        "slogan": "When it rains, I break the sky.",
        "weapon": ThunderstrikeGauntlet(),
        "flip": False,
        "abilities": {
            "F": Thunder(),
            "G": VolatileDefense(),
            "K": SilentButDeadly(),
            "L": OffensiveAura()
        }
    },
    {
        "name": "The Sleeper",
        "image": sleeper_image,
        "slogan": "Conquer the dreamscape: Rest, Rise, and Rule.",
        "weapon": DreamweaverBlade(),
        "flip": False,
        "abilities": {
            "F": Hibernation(),
            "G": PowerNap(),
            "K": RudeAwakening(),
            "L": DreamWalker()
        }
    },
    {
        "name": "Giggle One & Two",
        "image": giggle_image,
        "slogan": "Double the fun. Triple the chaos.",
        "weapon": (ChuckleChucks(), LaughingLasso()),
        "flip": False,
        "abilities": {
            "F": Giggle(),
            "G": GiggleOne(),
            "K": GiggleTwo(),
            "L": Mock()
        }
    }
]
# === Mode Selector ===
def select_mode():
    modes = ["Versus", "Training"]
    index = 0
    font = pygame.font.Font(None, 60)

    while True:
        screen.fill((0, 0, 0))
        title = font.render(f"Select Mode: {modes[index]}", True, (255, 255, 255))
        prompt = font.render("← → to Choose   ENTER to Confirm", True, (200, 200, 200))
        screen.blit(title, (240, 150))
        screen.blit(prompt, (180, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    index = (index - 1) % len(modes)
                elif event.key == pygame.K_RIGHT:
                    index = (index + 1) % len(modes)
                elif event.key == pygame.K_RETURN:
                    return modes[index]

        pygame.display.update()
        clock.tick(60)

# === Title Screen ===
def title_screen():
    font = pygame.font.Font(None, 80)
    sub_font = pygame.font.Font(None, 40)

    while True:
        screen.blit(title_bg, (0, 0))
        screen.blit(font.render("HECTIC HOMIES", True, (255, 255, 255)), (220, 100))
        screen.blit(sub_font.render("Press ENTER to Begin", True, (200, 200, 200)), (260, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                break

        pygame.display.update()
        clock.tick(60)

# === Character Selection ===
def select_character(player_label):
    index = 0
    font = pygame.font.Font(None, 40)
    big_font = pygame.font.Font(None, 60)

    while True:
        fighter = fighter_roster[index]
        screen.fill((20, 20, 20))
        screen.blit(fighter["image"], (300, 100))

        screen.blit(big_font.render(f"{player_label}: {fighter['name']}", True, (255, 255, 255)), (240, 30))
        screen.blit(font.render(f'"{fighter["slogan"]}"', True, (200, 200, 200)), (250, 310))
        screen.blit(font.render("← → to Choose    ENTER to Confirm", True, (150, 150, 150)), (200, 370))

        y = 330
        for key, ability in fighter["abilities"].items():
            screen.blit(font.render(f"{key}: {ability.name}", True, (180, 180, 180)), (250, y))
            y += 25

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    index = (index - 1) % len(fighter_roster)
                elif event.key == pygame.K_RIGHT:
                    index = (index + 1) % len(fighter_roster)
                elif event.key == pygame.K_RETURN:
                    return fighter_roster[index]

        pygame.display.update()
        clock.tick(60)

# === Map Selection ===
def select_map():
    maps = list(map_images.keys())
    index = 0
    font = pygame.font.Font(None, 60)

    while True:
        screen.fill((15, 15, 15))
        title_text = font.render(f"Select Stage: {maps[index]}", True, (255, 255, 255))
        prompt_text = font.render("← → to Choose   ENTER to Confirm", True, (200, 200, 200))
        screen.blit(title_text, (200, 150))
        screen.blit(prompt_text, (180, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    index = (index - 1) % len(maps)
                elif event.key == pygame.K_RIGHT:
                    index = (index + 1) % len(maps)
                elif event.key == pygame.K_RETURN:
                    return map_images[maps[index]]

        pygame.display.update()
        clock.tick(60)
# === Game Start Flow ===
title_screen()
chosen_mode = select_mode()

# === Mode Branching ===
if chosen_mode == "Versus":
    p1 = select_character("Player 1")
    p2 = select_character("Player 2")
    background = select_map()

    fighter_1 = Fighter(100, 300, p1["name"], p1["flip"], 1, p1["abilities"])
    fighter_1.combo_tracker = combo_tracker
    fighter_2 = Fighter(600, 300, p2["name"], True, 2, p2["abilities"])
    fighter_2.combo_tracker = combo_tracker

    combo_tracker = ComboTracker()
    game_state = "fight"
    winner = None

elif chosen_mode == "Training":
    trainee = select_character("Training Player")
    background = select_map()

    fighter_1 = Fighter(200, 300, trainee["name"], trainee["flip"], 1, trainee["abilities"])
    fighter_1.combo_tracker = combo_tracker
    dummy = Fighter(500, 300, "Training Dummy", False, 0, {})
    dummy.health = 9999
    dummy.weapon_type = "melee"

    combo_tracker = ComboTracker()
    game_state = "training"
    winner = None

# === Begin Main Loop Flag ===
run = True
WIDTH, HEIGHT = screen.get_size()
# === Main Game Loop ===
while run:
    clock.tick(60)

    if background:
        screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # === Versus Mode ===
    if game_state == "fight" and fighter_1 and fighter_2 and combo_tracker:
        fighter_1.move(fighter_2)
        fighter_2.move(fighter_1)

        fighter_1.update()
        fighter_2.update()

        fighter_1.draw(screen)
        fighter_2.draw(screen)

        pygame.draw.rect(screen, (255, 0, 0), (50, 50, fighter_1.health * 2, 20))
        pygame.draw.rect(screen, (255, 0, 0), (WIDTH - 250, 50, fighter_2.health * 2, 20))

        combo_tracker.update()
        combo_tracker.draw(screen, WIDTH)

        if fighter_1.health <= 0:
            winner = fighter_2.name
            ko_sound.play()
            combo_tracker.reset()
            game_state = "end"
        elif fighter_2.health <= 0:
            winner = fighter_1.name
            ko_sound.play()
            combo_tracker.reset()
            game_state = "end"

    # === Training Mode ===
    elif game_state == "training" and fighter_1 and dummy and combo_tracker:
        fighter_1.move(dummy)
        fighter_1.update()
        dummy.update()

        fighter_1.draw(screen)
        dummy.draw(screen)

        pygame.draw.rect(screen, (255, 0, 0), (50, 50, fighter_1.health * 2, 20))

        combo_tracker.update()
        combo_tracker.draw(screen, WIDTH)

    # === KO Screen ===
    elif game_state == "end":
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 80)

        if winner:
            win_text = font.render(f"{winner} Wins!", True, (255, 255, 0))
            screen.blit(win_text, (250, 150))

        prompt_text = font.render("Press R to Restart or Q to Quit", True, (200, 200, 200))
        screen.blit(prompt_text, (180, 250))
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        if fighter_1:
                            fighter_1.health = 100
                            fighter_1.rect.x = 100 if chosen_mode == "Versus" else 200
                        if chosen_mode == "Versus" and fighter_2:
                            fighter_2.health = 100
                            fighter_2.rect.x = 600
                        elif dummy:
                            dummy.health = 9999
                            dummy.rect.x = 500
                        if combo_tracker:
                            combo_tracker.reset()
                        game_state = chosen_mode.lower()
                        waiting = False
                    elif event.key == pygame.K_q:
                        waiting = False
                        run = False

    pygame.display.flip()

pygame.quit()
