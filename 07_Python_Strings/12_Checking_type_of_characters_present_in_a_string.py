# --------------------------------------------------------------------------------------------------
# ---------- To check type of characters present in a string -------------
# --------------------------------------------------------------------------------------------------

# 1. s.isalnum() : Returns True if all characters are (a-z,A-Z,0-9)
# 2. s.isalpha() : Returns True if all characters are only alphabet symbols (a-z,A-Z)
# 3. s.islower() : Returns True if all characters are lowercase alphabet symbols
# 4. s.isupper() : Returns True if all characters are uppercase alphabet symbols
# 5. s.isdigit() : Returns True if all characters are only digits
# 6. s.istitle() : Returns True if string is in title case
# 7. s.isspace() : Returns True if string contains only spaces

print("Durga786".isalnum()) # OUTPUT : True
print("Durga786".isalpha()) # OUTPUT : False
print("durga".isalpha()) # OUTPUT : True
print("durga".isdigit()) # OUTPUT : False
print("786786".isdigit()) # OUTPUT : True
print("abc".islower())  # OUTPUT : True
print("Abc".islower()) # OUTPUT : False
print("abc123".islower()) # OUTPUT : True
print("ABC".isupper()) # OUTPUT : True
print("Durga Software Solutions".istitle()) # OUTPUT : True
print("Durga software solutions".istitle()) # OUTPUT : False
print("      ".isspace()) # OUTPUT : True

# Q1. Write a program to check the type of character entered from the keyboard

s = input("Enter any character : ")
if s.isalnum():
    print("Its is alphanumeric charcter")
    if s.isalpha():
        print("It is alphabet symbol")
        if s.islower():
            print("It is lower case alphabet symbol")
        else:
            print("It is upper case alphabet symbol")
    else:
        print("It is a digit")
elif s.isspace():
    print("It is a space charater")
else:
    print("It is a non-space special character")