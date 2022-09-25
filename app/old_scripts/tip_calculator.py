print("""
This is tip calculator. Enter the information below to calculate the tip for your bill.
""")
bill = round(float(input("What is the total for the bill?: ")), 2)
party = int(input("How many in the party?: "))
tip = int(input("How much tip would you like leave? (10, 12, 15 or 20%?: "))


def calculate_tip(a, b, c):
    return round(float((((a / 100) * tip) + a) / party), 2)

print("Each person is responsible for: ")
print("$" + str(calculate_tip(bill, party, tip)))
print("$" + str(round(calculate_tip(bill, party, tip) * 3, 2)) + " is the total.")