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

# ==============================================================
# SORTING ELEMENTS OF LIST
# ==============================================================
# Sorting means arranging elements in a specific order.
# There are two ways to sort a list in Python:
#
# 1. sort()   -> Modifies the original list.
# 2. sorted() -> Creates and returns a new sorted list.

# ---------------------------------------------------------------------------------------
# 1. sort() : 
# ---------------------------------------------------------------------------------------
# Syntax: list_name.sort()

# Purpose: Sorts the elements of the list in-place (changes the original list).
#
# Default Behavior:
#     Numbers -> Ascending order (Small → Large)
#     Strings -> Alphabetical order (A → Z)

l = [20, 5, 15, 0, 10]
print("Before Sorting",l) # Output : [0, 5, 10, 15, 20]
l.sort() 
print("After Sorting",l) # Output :[0, 5, 10, 15, 20]

l = ['Banana', 'Cat', 'Apple']
print("Before Sorting",l) # Output : ['Banana', 'Cat', 'Apple']
l.sort() 
print("After Sorting",l) # Output : ['Apple', 'Banana', 'Cat']


# =====================================
# Sorting in Descending Order
# =====================================
# When you want to sort in descending order, you can use the reverse paraneter of the sort() method.

# Use:
#     list_name.sort(reverse=True)

# reverse=True means:
#     Numbers -> Largest → Smallest
#     Strings -> Reverse alphabetical order (Z → A)

l = [20, 5, 15, 0, 10]
print("Before Sorting",l) # Output : [20, 5, 15, 0, 10]
l.sort(reverse=True) 
print("After Sorting",l) # Output : [20, 15, 10, 5, 0]


l = ['Mango', 'Apple', 'Banana']
print("Before Sorting",l) # Output : ['Mango', 'Apple', 'Banana']
l.sort(reverse=True) 
print("After Sorting",l) # Output : ['Mango', 'Banana', 'Apple']


# ---------------------------------------------------------------------------------------
# Note :
# i. sort() method modifies the original list in-place and returns None.
# ii. If you want to use sort() method, all the list elements should be of same type only.
# iii. sort() is list specific method, it will not work for any other data structure.

# l = [40, 20, 'B', 'A']
# print("Before Sorting",l) # Output : [40, 20, 'B', 'A']
# l.sort() 
# print("After Sorting",l) # Output : TypeError: '<' not supported between instances of 'str' and 'int'
# ---------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------
# 2. sorted() Function :

# i. sorted() function returns a new sorted list and does not modify the  original list.
# ii. sorted() is a built-in function, it can be used with any iterable.

l1 = [20, 5, 15, 0, 10]
l2 = sorted(l1)
print("l1=>", l1) # Output : [20, 5, 15, 0, 10]
print("l2=>", l2) # Output : [0, 5, 10, 15, 20]
# ---------------------------------------------------------------------------------------

# ===============================================================================
# Descending Order with sorted()
# ===============================================================================
# Syntax:
#     sorted(iterable, reverse=True)
#
# Example:
#     sorted(l1, reverse=True)

l1 = [20, 5, 15, 0, 10]
l2 = sorted(l1, reverse=True)
print("l1=>", l1) # Output : [20, 5, 15, 0, 10]
print("l2=>", l2) # Output : [20, 15, 10, 5, 0]
# -------------------------------------------------------------------------------


# ===============================================================================
# Important Notes about sorted()
# ===============================================================================
# 1. Returns a NEW sorted list.
#
# 2. Original data remains unchanged.
#
# 3. Works with ANY iterable:
#      ✔ List
#      ✔ Tuple
#      ✔ String
#      ✔ Set
#      ✔ Dictionary (sorts keys by default)
#
# 4. Since it returns a new list, you can store it in a variable.
# -------------------------------------------------------------------------------

# ===============================================================================
# sort() vs sorted()
# ===============================================================================
#
# sort()
# ------
# ✔ List method
# ✔ Changes original list
# ✔ Returns None
# ✔ Slightly faster (no new list created)
#
# sorted()
# --------
# ✔ Built-in function
# ✔ Keeps original data unchanged
# ✔ Returns a new sorted list
# ✔ Works with any iterable
# -------------------------------------------------------------------------------