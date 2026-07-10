# ==================================================================================================
#                                Single Valued TUPLE
# ==================================================================================================


t = (10, 20, 30)
t = (10, 20)

t = (10) 
# this is int type and not tuple because tuple does not consider when only single number is present


print(type(t)) # Output : <class 'int'>


# What if intentionally we want to make it as a tuple
# Solution : Just add a comma

t = (10,)
print(type(t)) # Output : <class 'tuple'>


# Empty tuple
t = ()
print(type(t)) # Output : <class 'tuple'>


# Not tuple -> actually int type
t = (10) 
print(type(t)) # Output : <class 'int'>


# Clearly int type
t = 10
print(type(t)) # Output : <class 'int'>


t = (10,)
print(type(t)) # Output : <class 'tuple'>

t = 10,
print(type(t)) # Output : <class 'tuple'>


t = (10, 20, 30)
print(type(t)) # Output : <class 'tuple'>


t = 10, 20, 30
print(type(t)) # Output : <class 'tuple'>


t = (10, 20, 30,)
print(type(t)) # Output : <class 'tuple'>


t = 10, 20, 30,
print(type(t)) # Output : <class 'tuple'>

# ----------------------------------------------------------------------------------
# QUICK REVISION
# ----------------------------------------------------------------------------------

# (10)           -> int
# (10,)          -> tuple
# 10,            -> tuple
# ()             -> Empty Tuple
# (10,20,30)     -> tuple
# (10,20,30,)    -> tuple
# 10,20,30       -> tuple
# 10,20,30,      -> tuple
#
# Remember: "Comma creates Tuple, not Parentheses."
# ==================================================================================