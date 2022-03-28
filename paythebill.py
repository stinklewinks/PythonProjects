import random

print("""
**********************************************************
*                                                        *
*                   Welcome to Whose Bill                *
*                         Is It Anyway?                  *
*                                                        *
**********************************************************
""")
print("Please note, this app currently only works with a party of 4")
guests = []
num_guests = int(input("How many in your party?: "))

# Determine the number of guests and enter their names
if num_guests == 2:
    guests.append(input("Please enter the first name: "))
    guests.append(input("Please enter the second name: "))
elif num_guests == 3:
    guests.append(input("Please enter the first name: "))
    guests.append(input("Please enter the second name: "))
    guests.append(input("Please enter the third name: "))
elif num_guests == 4:
    guests.append(input("Please enter the first name: "))
    guests.append(input("Please enter the second name: "))
    guests.append(input("Please enter the third name: "))
    guests.append(input("Please enter the fourth name: "))
elif num_guests == 1:
    print("Well...not much to guess here...I guess I will oblige...")
    guests.append(input("Please enter the first name: "))
    print(f"{guests[0]} has to pay the bill. What are the odds!?")
else:
    print("That number of people isn't supported yet.")


# Determine who is gonna pay the bill
if 0 > len(guests) > 2:
    print("\nYou eating alone? Tell the house to take $5 on us. They know it's us...")
elif len(guests) == 2:
    wild_card = random.randint(0, 1)
    print(f"{guests[wild_card]} has to pay the bill.")
elif len(guests) == 3:
    wild_card = random.randint(0, 2)
    print(f"{guests[wild_card]} has to pay the bill.")
elif len(guests) == 4:
    wild_card = random.randint(0, 3)
    print(f"{guests[wild_card]} has to pay the bill.")
else:
    print("Unfortunately you did not enter a correct number. Please try again.")
