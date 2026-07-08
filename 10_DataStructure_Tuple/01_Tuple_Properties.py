# ==================================================================================================
#                                        TUPLE - NOTES
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# WHAT IS A TUPLE?
# --------------------------------------------------------------------------------------------------

# Tuple is a built-in Python data structure.
#
# It is almost exactly the same as a List.
#
# The only major difference is:
#
# ✔ List  -> Mutable
# ✔ Tuple -> Immutable
#
# If you already understand Lists well,
# Tuple becomes very easy because almost everything is identical.

# --------------------------------------------------------------------------------------------------
# REPRESENTATION OF TUPLE
# --------------------------------------------------------------------------------------------------

# Convention:
#
# Parentheses ()
#
# Example:
#
# t = (10, 20, 30)


# --------------------------------------------------------------------------------------------------
# IMPORTANT POINT
# --------------------------------------------------------------------------------------------------

# Parentheses are OPTIONAL.
#
# Example:
#
# t = 10, 20, 30
#
# Still considered as Tuple.


# Example
#
# >>> type(t)
#
# <class 'tuple'>

t = (10, 'durga', 20, 10)
t = 10, 'durga', 20, 10
print(t)
print(type(t)) # Output : <class 'tuple'>

# --------------------------------------------------------------------------------------------------
# PROPERTIES OF TUPLE
# --------------------------------------------------------------------------------------------------

# ✔ Order is preserved : Every element has a fixed position (index).
# ✔ Duplicates are allowed.
# ✔ Heterogeneous objects are allowed :  Different data types can exist together.

# ✔ Indexing is supported.
# Positive Index : 0  1  2  3
# Negative Index : -4 -3 -2 -1


# Example:

t = (10, 'durga', 20, 10)

print(t[0]) # Output : 10
print(t[1]) # Output : 20
print(t[2]) # Output : 30
print(t[-1]) # Output : 10

# ✔ Slicing is supported: Same as List.

# Example:

print(t[1:3]) # Output : ('durga', 20)
print(t[:]) # Output : (10, 'durga', 20, 10)
print(t[::-1]) # Output : (10, 20, 'durga', 10)





# --------------------------------------------------------------------------------------------------
# LIST VS TUPLE
# --------------------------------------------------------------------------------------------------

# +----------------------+----------------------------------+----------------------------------+
# | Feature              | List                             | Tuple                            |
# +----------------------+----------------------------------+----------------------------------+
# | Syntax               | []                               | () (optional)                    |
# | Example              | [10, 20, 30]                     | (10, 20, 30)                     |
# |                      |                                  | or 10, 20, 30                    |
# | Mutable              | Yes                              | No                               |
# | Immutable            | No                               | Yes                              |
# | Can Modify Elements? | Yes                              | No                               |
# | Order Preserved?     | Yes                              | Yes                              |
# | Duplicates Allowed?  | Yes                              | Yes                              |
# | Heterogeneous Data?  | Yes                              | Yes                              |
# | Indexing             | Supported                        | Supported                        |
# | Slicing              | Supported                        | Supported                        |
# | Append Elements      | Yes                              | No                               |
# | Remove Elements      | Yes                              | No                               |
# | Update Elements      | Yes                              | No                               |
# | Best Use Case        | Frequently changing data         | Fixed / Read-only data           |
# +----------------------+----------------------------------+----------------------------------+



# --------------------------------------------------------------------------------------------------
# WHAT IS MUTABLE?
# --------------------------------------------------------------------------------------------------

# Mutable means:
# Data can be changed after object creation.


# Example
#
# l = [10,20,30]
#
# l[0] = 777
#
# Output:
#
# [777,20,30]
#
# Therefore,
#
# List is Mutable.


# --------------------------------------------------------------------------------------------------
# WHAT IS IMMUTABLE?
# --------------------------------------------------------------------------------------------------

# Immutable means:
#
# Data cannot be changed after object creation.


# Example:

# t = (10,20,30)
# t[0] = 777  # Output: TypeError: tuple object does not support item assignment

# Therefore,Tuple is Immutable.



# --------------------------------------------------------------------------------------------------
# WHEN SHOULD WE USE LIST?
# --------------------------------------------------------------------------------------------------

# Use List when data changes frequently.
#
# Examples:
#
# ✔ YouTube Comments
# ✔ Facebook Comments
# ✔ Twitter Comments
# ✔ Shopping Cart
# ✔ Student List
#
# Because:
#
# • Add items
# • Remove items
# • Update items


# --------------------------------------------------------------------------------------------------
# WHEN SHOULD WE USE TUPLE?
# --------------------------------------------------------------------------------------------------

# Use Tuple when data is FIXED.
#
# Data is not expected to change.


# Examples:
#
# ✔ Vending Machine Accepted Coins
# ✔ Server States
# ✔ Week Days
# ✔ Months
# ✔ RGB Colors
# ✔ Fixed Configuration


# --------------------------------------------------------------------------------------------------
# PRACTICAL EXAMPLES
# --------------------------------------------------------------------------------------------------

# Example 1
#
# Accepted Coins
#
# (5, 10, 20)
#
# Machine accepts only these values.


# Example 2
#
# Server States
#
# (
#     "START",
#     "RUNNING",
#     "STOP",
#     "TERMINATED"
# )
#
# States are predefined.
# They never change.


# --------------------------------------------------------------------------------------------------
# QUICK REVISION
# --------------------------------------------------------------------------------------------------
# ✔ Tuple is almost same as List.
# ✔ Order is preserved.
# ✔ Duplicates are allowed.
# ✔ Heterogeneous objects are allowed.
# ✔ Indexing is supported.
# ✔ Slicing is supported.
# ✔ Tuple is Immutable.
# ✔ Parentheses are optional.
# ✔ Use List for changing data.
# ✔ Use Tuple for fixed data.