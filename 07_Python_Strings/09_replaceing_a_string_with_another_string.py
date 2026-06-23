# --------------------------------------------------------------------------------------------------
# ---------- replace() to perform replacement of one string with another string -------------
# --------------------------------------------------------------------------------------------------

# Syntax : s.replace(oldString, newString)

s = 'ABABABA'
s1=s.replace('A', 'B')
print(s1)   # Output: BBBBBBB


s = 'Durga Software Solutions'
s1=s.replace(' ', '')
print(s1)   # Output : DurgaSoftwareSolutions

print(s.count(' ')) # Output : 2

# without using count method, find number of spaces
print(len(s)-len(s1)) # Output : 2


# replace() method is case-sensitive

s = 'Learning Python is very Difficult'
s1 = s.replace('difficult', 'Easy')
print(s1)   # Output : Learning Python is very Difficult


# --------------------------------------------------------------------------------------------------
# String objects are immutable then how we can change the content by using replace() method?
# --------------------------------------------------------------------------------------------------


s = 'ABABABA'
s1=s.replace('A', 'B')
print(s)    # Output: ABABABA
print(s1)   # Output: BBBBBBB



s = 'ABABABA'
print("Before Replacement : "+s)    # Output: ABABABA
s=s.replace('A', 'B')
print("After Replacement : "+s)    # Output: ABABABA



# Many beginners think:
#
#     Original string "ABABABA"
#            ↓
#     Changed into "BBBBBBB"
#
# This is WRONG.
#
# Python NEVER changes the existing string object.

# ==========================================================
# WHAT ACTUALLY HAPPENS?
# ==========================================================

# Original object remains unchanged:

#        s
#        |
#        v
#    +---------+
#    | ABABABA |
#    +---------+

# replace() creates a BRAND NEW string object:

#        s
#        |
#        v
#    +---------+
#    | ABABABA |
#    +---------+
#
#
#        s1
#        |
#        v
#    +---------+
#    | BBBBBBB |
#    +---------+

# Therefore:
#
# Original object  -> still exists
# New object       -> created by replace()
#
# This is why strings are still immutable.