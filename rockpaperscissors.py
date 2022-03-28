import random

print("""
************************************************
*                                              *
*                                              *
*          Welcome to Rock, Paper,             *
*                & Scissors                    *
*                                              *
*                                              *
************************************************
""")


go = 'y'

while go == 'y':
    player_input = int(input("Choose 0 (for Rock), 1 (for Paper), and 2 (for Scissors): "))
    cpu_input = random.randint(0, 2)
    if player_input > cpu_input:
        if player_input == 2:
            print("""
            Scissors cuts paper. Player wins.
            """)
            go = input("Would you like to go again? y or n: ")
        if player_input == 1:
            print("""
            Paper covers rock. Player wins.
            """)
            go = input("Would you like to go again? y or n: ")
    if player_input < cpu_input:
        if player_input == 0 and cpu_input == 1:
            print("""
            Paper covers rock. CPU wins.
            """)
            go = input("Would you like to go again? y or n: ")
        if player_input == 0 and cpu_input == 2:
            print("""
            Rock crushes scissors. Player wins
            """)
            go = input("Would you like to go again? y or n: ")
        if player_input == 1 and cpu_input == 2:
            print("""
            Scissors cuts paper. CPU wins.
            """)
            go = input("Would you like to go again? y or n: ")
    if player_input == cpu_input:
        print("""
            Tie game. That's no good. You should go again.
        """)
        go = input("Would you like to go again? y or n: ")
