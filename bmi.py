weight = int(input("Please enter your weight in pounds (rounded to the nearest pound): "))
height = int(input("Thanks! Now, please enter your height in inches (rounded to the closest inch): "))
print("""
Thank you. Let me calculate your total...""")


def calc_bmi(a, b):
    return (a / (b**2)) * 703


print("Your results are printed below: ")
the_bmi = round(float(calc_bmi(weight, height)), 1)

if(the_bmi < 18.5):
    print("You are underweight.")
elif(18.5 < the_bmi < 25):
    print("You are in the normal range.")
elif(25 < the_bmi < 30):
    print("You are overweight.")
elif(30 < the_bmi < 35):
    print("You are obese")
else:
    print("You phat phuck")
