weight = int(input("Please enter your weight in pounds (rounded to the nearest pound): "))
height = int(input("Thanks! Now, please enter your height in inches (rounded to the closest inch): "))
print("""
Thank you. Let me calculate your total...""")


def calc_bmi(a, b):
    return (a / (b**2)) * 703


print("Your results are printed below: ")
print(round(float(calc_bmi(weight, height)), 1))
