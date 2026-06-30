# ==================================================================================================
#                                   LIST OPERATORS
# ==================================================================================================
#
# In this lecture, we will learn three important operators that can be used with Python lists:
#
#   1. Equality Operators     -> ==, !=
#   2. Relational Operators   -> <, <=, >, >=
#   3. Membership Operators   -> in, not in
#
# ==================================================================================================



# ==================================================================================================
#                              EQUALITY OPERATORS (==, !=)
# ==================================================================================================
#
# Equality operators are used to check whether two lists are equal or not.
#
# A list is considered equal ONLY IF:
#
#   ✅ 1. Both lists contain the same number of elements.
#   ✅ 2. Elements appear in the same order.
#   ✅ 3. Every element has exactly the same value (Case Sensitive).
#
# NOTE:
# Python compares strings in a case-sensitive manner.
# "Dog" and "DOG" are considered different.
#
# Example:
# ['Dog', 'Cat'] == ['Dog', 'Cat']   -> True
# ['Dog', 'Cat'] == ['DOG', 'CAT']   -> False
# ['Dog', 'Cat'] == ['Cat', 'Dog']   -> False
#
# The != operator simply checks whether two lists are NOT equal.
#
# ==================================================================================================


l1 = ['Dog', 'Cat', 'Rat']
l2 = ['Dog', 'Cat', 'Rat']
l3 = ['DOG', 'CAT', 'RAT']
l4 = ['Cat', 'Rat', 'Dog']

print(l1 == l2)   # True  -> Everything is exactly the same.
print(l1 == l3)   # False -> Different letter case.
print(l1 == l4)   # False -> Same elements but different order.
print(l1 != l4)   # True  -> Lists are not equal.

print("-----------------------------------------")


# ==================================================================================================
#                           RELATIONAL OPERATORS (<, <=, >, >=)
# ==================================================================================================
#
# Relational operators compare two lists.
#
# IMPORTANT:
# Python DOES NOT compare lists based on their length.
#
# Instead, it compares the elements one by one from LEFT TO RIGHT.
#
# Comparison Process:
#
# Step 1:
# Compare the first elements.
#
# If they are different:
#     Decision is made immediately.
#
# If they are equal:
#     Move to the second element.
#
# Continue until a different element is found.
#
# Example:
#
# [10,20,30]  <  [50,60]
#
# Compare:
#
# 10 vs 50
#
# Since 10 < 50,
# Python immediately returns True.
#
# Remaining elements are NOT checked.
#
# ------------------------------------------------------------------------------------
# If all compared elements are equal but one list has extra elements:
#
# [10,20] < [10,20,30]
#
# Since the first list ends first,
# it is considered smaller.
#
# ------------------------------------------------------------------------------------
# For String Lists:
#
# Strings are compared alphabetically (Lexicographical Order).
#
# Example:
#
# "Roja" > "Ramba"
#
# Compare:
#
# R == R
# o > a
#
# Therefore,
# "Roja" is greater.
#
# ==================================================================================================


l1 = [10, 20, 30, 40]
l2 = [50, 60]

print(l1 < l2)    # True  -> 10 < 50
print(l1 <= l2)   # True
print(l1 > l2)    # False
print(l1 >= l2)   # False


l1 = ['Ramba', 'Ramya']
l2 = ['Roja', 'Sunny']

print(l2 > l1)    # True -> Alphabetical comparison ("Roja" > "Ramba")

print("-----------------------------------------")


# ==================================================================================================
#                           MEMBERSHIP OPERATORS (in, not in)
# ==================================================================================================
#
# Membership operators are used to check whether an element exists in a list.
#
# in
# ----
# Returns True if the element is present.
#
# not in
# -------
# Returns True if the element is NOT present.
#
# These are among the most commonly used operators while working with lists.
#
# Example:
#
# 10 in [10,20,30]
# True
#
# 50 not in [10,20,30]
# True
#
# 70 in [10,20,30]
# False
#
# ==================================================================================================


l1 = [10, 20, 30, 40]

print(10 in l1)        # True  -> 10 exists in the list.
print(50 not in l1)    # True  -> 50 does not exist.
print(70 in l1)        # False -> 70 is not present.