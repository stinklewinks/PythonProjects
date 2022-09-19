import time
import sys
from modules import level_one
from player_creation import skills
from modules.player_class import Player

game_switch = "y"

# TODO: Create a better while switch.  This one is broken
# TODO: Create an ENEMY class. 
# TODO: Create an interactive opening script

while game_switch == "y":
    time.sleep(1)
    print(""" Welcome to the text-based game: Andalon's Mirror.
    This game is brought to you by BERYLSOFT.
    """)
    time.sleep(2)
    print("This is the first game in the trilogy.")
    time.sleep(1)
    game_switch = input("Would you like to play? [y or n]: ")

    new_player = Player()
    new_player.name = input("What will your character's name be?: ")
    print("Your name will be " + new_player.name)


    print(new_player.evade())

    sys.exit()