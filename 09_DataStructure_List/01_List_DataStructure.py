# --------------------------------------------------------------------------------------------------
# ---------- List Data Structure -------------
# --------------------------------------------------------------------------------------------------

# If we want to represent a group of objects as a single entity where duplicates are allowed and 
# insertion order must be preserved, then we require to go for list data structure

# Note : 
# Different type of objects (heterogenous objects) are also allowed
# List is dynamic
# List is mutable
# Representation with square brackets []

# SYNTAX :

# Empty List 
l = []

# Insertion

l.append(10)
l.append('durga')
l.append(10)

print(l) # OUTPUT : [10, 'durga', 10]

l[0] = 77
print(l) # OUTPUT : [77, 'durga', 10]