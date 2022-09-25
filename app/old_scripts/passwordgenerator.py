import random
import string

print("""
Welcome to your very own password generator! Please enter some information below and you will have
your password generated in no time!
""")

MAX_LIMIT = 255
the_password = ""
pass_length = int(input("Select a difficulty level? (1-10): "))
symbol_count = input("Would you like to include symbols? y or n: ")
num_count = input("How many symbols would you like to include? y or n: ")
chars = string.ascii_letters
new_chars = chars.split(" ")
the_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
the_symbols = [')', '!', '@', '#', '$', '%', '^', '&', '*', '(', '.']
chars_list = []

for _ in chars:
    chars_list.append("")

if pass_length:
    new_pass = []
    counter = 0
    while counter < pass_length:
        if symbol_count == 'y' and num_count == 'y':
            new_pass.append(new_chars[0][round(random.randint(0, 51))])
            new_pass.append(the_numbers[round(random.randint(0, 9))])
            new_pass.append(the_symbols[round(random.randint(0, 10))])
            counter += 1
            the_new_password = ''.join([str(item) for item in new_pass])
        else:
            new_pass.append(new_chars[0][round(random.randint(0, 51))])
            counter += 1
            the_new_password = ''.join([str(item) for item in new_pass])
    
    print("Your new password: ")
    print(the_new_password)
else:
    print("You did not specify a length. Program aborted.")
