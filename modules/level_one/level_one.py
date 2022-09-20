import time
import sys
#level_one_notes = open('./modules/level_one/level one.txt', 'r')
level_one_notes = open('level one.txt', 'r')

level_one_opening_txt = level_one_notes.readlines()

def level_one_opening():
    time.sleep(2)
    print(level_one_opening_txt[0])
    time.sleep(2)
    print(level_one_opening_txt[1])
    time.sleep(2)
    print(level_one_opening_txt[2])
    print(level_one_opening_txt[3])
    print(level_one_opening_txt[4])
    print(level_one_opening_txt[5])
    print(level_one_opening_txt[6])

def opening_choice(user_input):
    the_switch = 'on'
    while the_switch == 'on':
        if isinstance(user_input, str):
            return 'You must input a number. Try again.'
        elif user_input == 1:
            the_switch = 'off'
            return """ There are 3 rooms: The main room, a vacant room and the kitchen. """
        elif user_input == 2:
            the_switch == 'off'
            return """ You see four people."""

def portal():
    new_player.location = 'Portal'

# TODO: Figure out a way to decipher whether or not user enters something other than 1-4
level_one_opening()
choice_input = int(input("Enter your choice [1-4]: "))
print(opening_choice(choice_input))