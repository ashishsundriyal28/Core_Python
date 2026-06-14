# --------------------------------------------------------------------------------------------------
# ---------- String Methods : find(), rfind() -------------
# --------------------------------------------------------------------------------------------------

# If you want to find index of the given substring then four methods are available in python.
# They are : find(), rfind(), index(), rindex()

s = 'ABCBA'

# find() method : 
# always searches for the substring from left to right
# if found, returns only the first occurance index of the substring from the beginning of the string
# if not found, returns -1
print(s.find('B'))  # Output: 1
print(s.find('C'))  # Output: 2
print(s.find('D'))  # Output: -1


# rfind() method : returns the highest index of the substring if found in given string. If not found, returns -1
# always searches for the substring from right to left
# if found, returns the first occurance index of the substring from the end of the string
print(s.rfind('B'))  # Output: 3
print(s.rfind('D'))  # Output: -1 

# ----------------------------------------------------------------------------------
# How to search in a specific range using find() and rfind() methods
# both methods accept two optional parameters : start and end
# which means, search for the substring from index 'start' to index 'end-1'
# -----------------------------------------------
# SYNTAX : string.find(substring, start, end)
# SYNTAX : string.rfind(substring, start, end)
# -----------------------------------------------
s = 'ABCDEFGHIJBK'
print(s.find('B', 3, 11))   # Output: 9  (searches for 'B' between index 3 and 10)
print(s.rfind('F', 3, 8))  # Output: 5  (searches for 'F' between index 3 and 6)
# ----------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------
# ---------- String Methods : index(), rindex() -------------
# --------------------------------------------------------------------------------------------------


# index() method : 
# returns the lowest index of the substring if found in given string. 
# If not found, raises ValueError

# rindex() method : 
# returns the highest index of the substring if found in given string.

# ----------------------------------------------------------------------------------
s = 'ABCBA'
print(s.index('B')) # Output : 1
# print(s.index('Z')) # Output : ValueError: substring not found

print(s.rindex('B')) # Output : 3
# print(s.rindex('Z')) # Output : ValueError: substring not found
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# EXAMPLE : 
# mail = input('Enter your mail id : ')

# try:
#     i = mail.index('@')
#     print('mail id contains @')
# except ValueError:
#     print('mail id does not contain @')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
s = 'ABCDEFGHIJKLMN'

# print(s.index('B', 4, 8)) # Output : ValueError : substring not found
print(s.index('F', 4, 8)) # Output : 5
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
s = 'ABCDE'

print(s.index('D', 2, 100)) 

# STILL CORRECT : 
# it will eventually find the substring (here, D) from index 2 to last index 
# upper limit can be any number, if greater than the length of the string, 
# it will consider the last index 
# ----------------------------------------------------------------------------------
