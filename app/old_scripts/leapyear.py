print("""
************************************
*                                  *
* This is the Leap Year Calculator *
*                                  *
************************************
""")

year = int(input("Pick a four digit year: "))


if(year % 4 == 0):
    print("Leap Year")
elif(year % 100 == 0):
    if (year % 400 == 0):
        print("leap Year")
    else:
        print("Not Leap Year")
else:
    print("Not Leap Year")
