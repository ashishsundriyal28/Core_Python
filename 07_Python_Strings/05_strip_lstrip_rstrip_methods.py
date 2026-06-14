# --------------------------------------------------------------------------------------------------
# ---------- String Methods : strip(), lstrip(), rstrip() -------------
# --------------------------------------------------------------------------------------------------

# example code : 

city = input("Enter your city name: ")

if city == "Hyderabad":
    print("Hello Hyderabadi, Aadaab!")
elif city == "Chennai":
    print("Hello Madrasi, Vanakkam!")
elif city == "Bangalore":
    print("Hello Kannadiga, Namaskara!")
else:
    print("your city is invalid !!")

# problem with above code : if user enters extra spaces before or after the city name, for example : "   Hyderabad  "
# then the above code will not work as expected as python considers the extra spaces as part of the string.

# Solution : use lstrip(), rstrip(), strip() method to remove extra spaces from both ends of the string
# lstrip() : removes extra spaces from the left side of the string
# rstrip() : removes extra spaces from the right side of the string
# strip()  : removes extra spaces from both sides of the string


city = input("Enter your city name: ")
scity = city.strip()  # using strip() method to remove extra spaces from both ends

if scity == "Hyderabad":
    print("Hello Hyderabadi, Aadaab!")
elif scity == "Chennai":
    print("Hello Madrasi, Vanakkam!")
elif scity == "Bangalore":
    print("Hello Kannadiga, Namaskara!")
else:
    print("your city is invalid !!")