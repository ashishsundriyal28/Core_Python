# ==================================================================================================
#                                Creation of TUPLE
# ==================================================================================================

# -------------------------------------
# 1. Empty Tuple
# -------------------------------------

# Syntax:
# t = ()


# -------------------------------------
# 2. Single-Valued Tuple
# -------------------------------------

# Syntax:
# t = (10,)

# Important:
# • Comma (,) creates the tuple, NOT the parentheses.
# • (10) is just an integer enclosed in parentheses.
# • (10,) is a tuple containing one element.

# Examples:
# t = (10,)   # Tuple
# t = 10      # Integer

# -------------------------------------
# 3. Multi-Valued Tuple
# -------------------------------------

# Valid ways:
# t = (10, 20, 30)
# t = 10, 20, 30
# t = (10, 20, 30,)
# t = 10, 20, 30,

# Notes:
# • Parentheses are optional.
# • Trailing comma is allowed.
# • Python automatically packs comma-separated values into a tuple (Tuple Packing).


# -------------------------------------
# 4. Creating Tuple using tuple()
# -------------------------------------
# If you want to create an equivalent tuple 
# for any given sequence then we go for tuple() function

# Syntax
# t = tuple(sequence)

# Purpose: Converts any iterable into a tuple.

# Common Iterables:
# • list
# • string
# • range
# • set
# • dictionary (keys only)


# Example 1
l = [10, 20, 30]
t = tuple(l)
print(t) # Output : (10, 20, 30)

# Example 2
t = tuple(range(1,11,2))
print(t) # Output : (1, 3, 5, 7, 9)

# tuple() converts any iterable into a tuple, 
# and since a string is iterable, each character becomes a separate tuple element.
t = tuple('ashish')
print(t) # Output : ('a', 's', 'h', 'i', 's', 'h')


# -------------------------------------
# Dynamic Input
# -------------------------------------

t = eval(input('Enter tuple of values'))

print(t) # Output : (10, 20, 30)
print(type(t)) # Output : <class 'tuple'>

# Notes:
# • eval() evaluates the entered input as a Python expression.
# • If user enters tuple syntax, a tuple object is created.
# • Avoid eval() with untrusted input because it can execute arbitrary Python code.
