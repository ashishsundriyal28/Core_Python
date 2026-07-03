# ==================================================================================================
#                                   ORDERING ELEMENTS OF LIST
# ==================================================================================================
#
# Python provides TWO ways to reverse the order of elements:
#
#     1️⃣. reverse()   → List Method
#     2️⃣. reversed()  → Built-in Function
#
# Although both are used for reversing elements, they work differently.
#

# --------------------------------------------------------------------------------------------------
# 1. reverse() : 
# --------------------------------------------------------------------------------------------------
# Reversing the order of elements present in the list.
#
# Syntax:
# list_name.reverse()

# Note : 
# i. IT IS A LIST SPECIFIC METHOD (WILL NOT WORK FOR ANY OTHER DATA STRUCTURE)
# It is not going to create any new object, it will reverese the existing list only

l = [10, 20, 30, 40]
print(f'Before Reversal : {l}')  # Output: [10, 20, 30, 40]
l.reverse()
print(f'After Reversal : {l}')  # Output: [40, 30, 20, 10]


# ==================================================================================================
# 2. reverse() vs reversed()
# ==================================================================================================

# reverse() : 
# It is a list specific method, 
# it will reverse the existing list only 
# will not create any new object 
# Example : explained above 


# reversed() : 
# It is a built-in function, 
# it will return an iterator that yields the elements of the list in reverse order 
# it will not modify the original list 
# will create a new object (iterator) 
# used for reversing any iterable (list, tuple, string etc.)

l = [10, 20, 30, 40]

r = reversed(l)     # r = reversed object iterator
print(r)    # Output : <list_reverseiterator object at 0x000001ED45A11360>

l1 = list(r)        # converting iterator to list
print(l)    # Output : [10, 20, 30, 40]
print(l1)   # Output : [40, 30, 20, 10]



# ==================================================================================================
# Using reversed() with Strings
# ==================================================================================================
# Strings are IMMUTABLE.
# Therefore, strings do NOT have reverse() method.

s = 'durga'
# s.reverse() # Output: AttributeError: 'str' object has no attribute 'reverse'
r = reversed(s)

for x in r:
    print(x, end='') # Output : agrud

# ==================================================================================================
# When to use reverse() ?
# ==================================================================================================
#
# ✔ When you want to modify the original list.
# ✔ When you no longer need the previous order.
# ✔ When working only with lists.
# ✔ Slightly more memory efficient.
#
# Example:
#
# numbers.reverse()
#


# ==================================================================================================
# When to use reversed() ?
# ==================================================================================================
#
# ✔ When original data should remain unchanged.
# ✔ When working with strings, tuples, ranges, etc.
# ✔ When you only want to iterate in reverse order.
# ✔ When you need a reversed copy.
#
# Example:
#
# for x in reversed(numbers):
#     print(x)
#

"""
==========================================================================================================
                                           🚫 Common Mistakes
==========================================================================================================

+-------------+---------------------------------------------+-----------------------------------------------+
| Mistake     | Code                                        | Explanation                                   |
+=============+=============================================+===============================================+
| ❌ Mistake 1| l = [10, 20, 30]                            | reverse() modifies the original list          |
|             |                                             | IN-PLACE and ALWAYS returns None.             |
|             | x = l.reverse()                             |                                               |
|             | print(x)                                    | Output: None                                  |
+-------------+---------------------------------------------+-----------------------------------------------+
| ❌ Mistake 2| s = "Python"                                | reverse() is available ONLY for list.         |
|             |                                             |                                               |
|             | s.reverse()                                 | Strings are immutable and therefore           |
|             |                                             | do not provide a reverse() method.            |
|             |                                             |                                               |
|             |                                             | Output:                                       |
|             |                                             | AttributeError:                               |
|             |                                             | 'str' object has no attribute 'reverse'       |
+-------------+---------------------------------------------+-----------------------------------------------+
| ❌ Mistake 3| l = [10, 20, 30]                            | reversed() returns a Reverse Iterator,        |
|             |                                             | NOT a list.                                   |
|             | r = reversed(l)                             |                                               |
|             | print(r)                                    | Output:                                       |
|             |                                             | <list_reverseiterator object at 0x...>        |
|             |                                             |                                               |
|             | Correct Way                                 |                                               |
|             | ------------                                |                                               |
|             | print(list(r))                              | [30, 20, 10]                                  |
+-------------+---------------------------------------------+-----------------------------------------------+

💡 Remember
-----------
✔ reverse()  → Modifies the original list and returns None.
✔ reversed() → Returns an iterator; convert it using list(), tuple(), etc.
✔ reverse()  → Works ONLY with list.
✔ reversed() → Works with almost every iterable.

==========================================================================================================
"""