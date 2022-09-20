import time
import sys
from modules.level_one.level_one import level_one_opening
from player_creation.skills import magic_skills
from modules.player_class import Player

game_notes = open('game mode.txt', 'r')
opening = game_notes.readlines()

game_switch = "y"
rules_switch = "n"
# TODO: Create an ENEMY class. 
# TODO: Create an interactive opening script
time.sleep(1)
print(opening[0])
time.sleep(2)
print("This game is brought to you by BERYLSOFT")
time.sleep(1)
print("This is the first game in the trilogy.")
time.sleep(1)
rules_switch = input("Would you like to read the rules? [y or n]: ")

while rules_switch == "y":
    time.sleep(2)
    print(opening[5])
    time.sleep(2)
    print(opening[7])
    time.sleep(2)
    print(opening[9])
    time.sleep(2)
    print(opening[11])
    time.sleep(2)
    rules_switch = input("Would you like to see the rules again? [y or n]: ")

game_switch = input("Would you like to play? [y or n]: ")

while game_switch == "y":
    new_player = Player()
    new_player.name = input("What will your character's name be?: ")
    print(f"Your name will be {new_player.name}")

    time.sleep(2)
    level_one_opening()
    
    sys.exit(0)
