# --------------------------------------------------------------------------------------------------
# ------------------------------- String Slicing --------------------------------------
# --------------------------------------------------------------------------------------------------


# Example : abcdefghijklmnopqrstuvwxyz
# => def, jklm etc are slices

# SYNTAX : string[begin:end:step]
# => returns substring from begin to end-1
# => step argument is optional
# => begin argument is optional and default value is 0
# => end argument is optional and default value is len(string) 

s = "abcdefghijklmnopqrstuvwxyz"

print(s[2:7])
print(s[:7])
print(s[2:])

print("TOTAL STRING => "+s[:])

# with step
print(s[2:7:1])
print(s[2:7:2])


# step argument examples
print("=>",s[::1])
print(s[::2])
print(s[::3])


# -----------------------
# Slicing Rules 
# -----------------------

# string[begin:end:step]

# step value can be either positive (+ve) or negative (-ve)

# If step is +ve:
    # Left to Right (Forward direction), begin to end-1
# If step is -ve:
    # Right to Left (Backward direction), begin to end+1

# NOTES :
# ** In forward direction, if end value is 0, then result is always empty 
# ** In backward direction, if end value is -1, then result is always empty 

# Either forward direction or backward direction, we can take both +ve and -ve values for begin and end index


# In forward direction:
# default value for begin: 0
# default value for end: len(s)

# In backward direction:
# default value for begin: -1
# default value for end : -len(s) + 1


S='abcdefghij'
s[1:6:2]
s[ : :1]
s[ : : -1]
s[3:7 :- 1]
s[7:4 :- 1]
s[0:10000:1]
s[-4:1 :- 1]
s[-4:1 :- 2]
s[5:0:1]
# s[9:0:0]
s[0 :- 10 :- 1]
s[0 :- 11 :- 1]
s[0:0:1]

print(s[10:-1:-1])
print(s[5:-1:-1])
print(s[10000:2:-1])