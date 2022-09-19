import time
import sys
from modules import level_one
from player_creation.skills import magic_skills
from modules.player_class import Player

game_switch = "y"
# TODO: Create an ENEMY class. 
# TODO: Create an interactive opening script
time.sleep(1)
print(""" Welcome to the text-based card game: Andalon: War Game.
This game is brought to you by BERYLSOFT.
""")
time.sleep(2)
print("This is the first game in the trilogy.")
time.sleep(1)
game_switch = input("Would you like to play? [y or n]: ")

while game_switch == "y":
    new_player = Player()
    new_player.name = input("What will your character's name be?: ")
    print(f"Your name will be {new_player.name}")


    print(new_player.add_skill('Shock'))
    new_player.add_skill(magic_skills[0])
    print(new_player.skills)
    
    sys.exit(0)
