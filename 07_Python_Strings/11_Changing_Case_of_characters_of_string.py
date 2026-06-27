# --------------------------------------------------------------------------------------------------
# ---------- Changing Case of Characters of Strings -------------
# --------------------------------------------------------------------------------------------------

s = "Learing Python is very easy"

# 1. upper() : To convert all characters to upper case
print(s.upper()) # OUTPUT : LEARING PYTHON IS VERY EASY


# 2. lower() : To convert all characters to upper case
print(s.lower()) # OUTPUT : learing python is very easy


# 3. swapcase() : To convert lower case characters to upper case 
# and upper case characters to lower case
print(s.swapcase()) # OUTPUT : lEARING pYTHON IS VERY EASY


# 4. title() : To convert all characters to title case. 
# ie. first character in every word should be upper case 
# and all remaining characters should be in lower case
print(s.title()) # OUTPUT : Learing Python Is Very Easy


# 5. capitalize() : Only first character will be converted to upper case and 
# all remaining characters can be converted to lower case
print(s.capitalize()) # OUTPUT : Learing python is very easy


# Ques 1. Write a program to check whether the given 2 Strings 
# are equal or not by ignoring case

# # Way 1
# s1 = input("Enter first String : ")
# s2 = input("Enter second String : ")

# if s1.lower() == s2.lower():
#     print("Both Strings are equal")
# else:
#     print("Both strings are not equal")

# # Way 2
# s1 = input("Enter first String : ").lower()
# s2 = input("Enter second String : ").lower()

# if s1 == s2:
#     print("Both Strings are equal")
# else:
#     print("Both strings are not equal")


# Q2. Write a program To check whether provided username and password 
# are valid or not? # username is not case sensitive, 
# but password should be case sensitive

# username = input("Enter username : ")
# pwd = input("Enter password : ")

# if username.lower() == "durga" and pwd == "anushka":
#     print("Valid user")
# else:
#     print("Invalid user")


# Q3. Write a program to convert first and last characters as upper case and 
# all remaining characters should be lower case of the given string?

# s = "durga"
# output = s[0].upper() + s[1:len(s)-1].lower() + s[-1].upper()
# print(output)


# --------------------------------------------------------------------------------------------------
# ---------- Checking starting and ending part of the String -------------
# --------------------------------------------------------------------------------------------------

# 1. s.startswith(substring)
# Returns True if the string starts with provided substring

# 2. s.endswith(substring)
# Returns True if the string ends with provided substring

s = "Learing Python is very easy"

print(s.startswith("Learing"))
print(s.startswith("Lea"))
print(s.startswith("lea"))
print(s.endswith("easy"))
print(s.endswith("Easy"))