# --------------------------------------------------------------------------------------------------
# ---------- Mathmatical, Membership and Comparison Operators for Strings -------------
# --------------------------------------------------------------------------------------------------

# + operator -> concatenates two strings
# * operator -> repeats a string a specified number of times

s1 = "Hello"
s2 = "World"

# Concatenation
# both should be string types
s3 = s1 + " " + s2 
print(s3)  # Output: Hello World

# Repetition
# One should be string type and the other should be integer type only
s4 = s1 * 3
s5 = 4 * s1
print(s4)  # Output: HelloHelloHello
print(s5)  # Output: HelloHelloHelloHello

# Membership Operators
# 'in' operator checks if a substring exists within a string
# not in operator checks if a substring does not exist within a string

# 'in' operator
s6 = "World"
print('d' in s3)  # Output: True
print('z' in s3)  # Output: False

# not in operator
print('z' not in s3)  # Output: True

'''
s = input("Enter a string: ")
substring = input("Enter a substring to check: ")
# Check if the substring is in the string
if substring in s:
    print(f"'{substring}' is found in '{s}'")
else:
    print(f"'{substring}' is not found in '{s}'")
'''

# Comparison Operators
# Unicode comparison is used for strings in Python
# Comparison operators compare two strings lexicographically
# '==' operator checks if two strings are equal
# '!=' operator checks if two strings are not equal
# '<' operator checks if one string is lexicographically less than another
# '>' operator checks if one string is lexicographically greater than another
# '<=' operator checks if one string is lexicographically less than or equal to another
# '>=' operator checks if one string is lexicographically greater than or equal to another

if 'durga' < 'ravi':
    print("'durga' is lexicographically less than 'ravi'")
else:
    print("'durga' is not lexicographically less than 'ravi'")



s1 = input("Enter a string 1: ")
s2 = input("Enter a string 2: ")
# Check if the substring is in the string
if s1 == s2:
    print("Both equal")
elif s1 < s2:
    print("s1 is less than s2")
else:
    print("Both not equal")