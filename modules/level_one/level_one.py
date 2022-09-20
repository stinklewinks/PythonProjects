import time
import sys
level_one_notes = open('./modules/level_one/level one.txt', 'r')

level_one_opening_txt = level_one_notes.readlines()

def level_one_opening():
    time.sleep(2)
    print(level_one_opening_txt[0])
    time.sleep(2)
    print(level_one_opening_txt[1])

def portal():
    new_player.location = 'Portal'
