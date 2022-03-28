print("""
********************************************
*                                          *
*   Welcome to the Simple Pizza Maker      *
*                                          *
*         dev: StinkleWinks                *
*                                          *
********************************************
""")

small_pizza = 15
med_pizza = 20
lrg_pizza = 25

pepperoni = 2
extra_cheese = 1

pizza_order = input("What size pizza would you like?: S, M or L: ")
toppings = input("Would you like to add pepperoni? Y or N: ")
add_extra_cheese = input("Wanna cheese it up for an extra $1? Y or N: ")

if pizza_order == 'S':
    if toppings == 'Y':
        if add_extra_cheese == 'Y':
            total = small_pizza + pepperoni + extra_cheese
            print("You owe: " + str(round(float(total), 2)))
        else:
            total = small_pizza + pepperoni
            print("You owe: " + str(round(float(total), 2)))
    else:
        if add_extra_cheese == 'Y':
            total = small_pizza + extra_cheese
            print("You owe: " + str(round(float(total), 2)))
        else:
            total = small_pizza
            print("You owe: " + str(round(float(total), 2)))
else:
    print("You ordered something else.")

# Need to add the same functionality for Medium and Large Pizzas
#
# Will add functionality for:
#           -More Toppings
#           -Delivery Cost
#           -Adding Tip
