print("""
Welcome to the Odd or Even game. I will tell you whether your number is odd or even. Let's go!
""")

the_number = input("Pick any whole number: ")

if(int(the_number) % 2 == 0):
    print("Even")
else:
    print("Odd")


print("Wasn't that cool!?")
