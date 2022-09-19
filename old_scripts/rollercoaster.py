print("""
Welcome to Stinkle land! This script will determine if you are tall enough to ride Stinkle's Cyclone
and how much tickets and a ride photo will cost!
""")

height = int(input("First, how tall are you (in inches)?: "))
age = int(input("Thank you. Now please enter your age (whole numbers please): "))
vip_package = input("Did you get the VIP package at sign up?: Y or N: ")

if height < 48 and age < 12:
    print("Sorry, you cannot ride this ride. Reasons: ")
    print("-Does not meet height requirements", "\n", "-Does not meet age requirements")
elif height < 48:
    print("Sorry, you are too short for this ride.")
elif age < 12:
    print("Sorry, you are too young for this ride.")
else:
    # Will add more parameters to make a more complex determination
    # ex -> using a type of Regex or something to make sure only Y and N values can be processed
    # Perhaps a while loop that cancels once one of those characters are entered
    if height > 48 and age > 12:
        answer =  str(input("Would you like to buy a ride photo?: Y or N?: "))
        if answer == 'Y':
            print("\nYou want a picture!")
            if age < 12:
                print("Kids get pictures for free.")
            elif 12 > age > 18:
                print("You get the teenager discount. $4.")
            else:
                print("Adult photos are an additional $14.")
        else:
            print("You do not want a picture")

if vip_package == 'Y':
    print("Thank you for purchasing the VIP Package. You are the best!")
else:
    print("You cheapskate! You didn't buy the VIP package. Loser.")
