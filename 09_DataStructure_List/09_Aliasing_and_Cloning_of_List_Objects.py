# ==================================================================================================
#                                   ALIASING AND CLONING OF LIST OBJECTS
# ==================================================================================================

l1 = [10, 20, 30, 40]       # -> l1 points to a new list object
l2 = l1                     # -> l2 is a new reference variable
                            # -> pointing to the SAME list object as l1

# (i.e., both l1 and l2 refer to the same list in memory)

# because of this line, a new reference variable will be created regarding to the existing list object
# basically, a new variable pointing to the same list object will be created

# ------------------------------------------------------------------------------
# BEFORE: l2 = l1
#
#    l1 ----------------------->  +-----------------------------+
#        (reference)              |  [ 10 | 20 | 30 | 40 ]      |
#                                 +-----------------------------+
#                                   List Object (in memory)
#                                   id: 0x7fa4c1b8a640
#
# ------------------------------------------------------------------------------
# AFTER: l2 = l1
#
#    l1 ----------------------->  +-----------------------------+
#        (reference)              |  [ 10 | 20 | 30 | 40 ]      |
#                                 +-----------------------------+
#    l2 ----------------------->     List Object (in memory)
#        (reference)                 id: 0x7fa4c1b8a640
#
# ------------------------------------------------------------------------------
# KEY POINTS:
#
# 1. l1 and l2 are two different variables (references).
# 2. Both l1 and l2 point to the SAME list object in memory.
# 3. No new list object is created by the assignment (l2 = l1).
# 4. Any changes made through l1 or l2 will reflect in the same list.
#
# Example:
#
#     l2.append(50)
#
#     print(l1)    # [10, 20, 30, 40, 50]
#     print(l2)    # [10, 20, 30, 40, 50]
#
# ------------------------------------------------------------------------------

# Aliasing : the process of creating duplicate reference variable
# => Another name for the existing list object is called aliasing

# If we change the content of the list, 
# automatically the change will be reflected to other reference variable

# If we make change using l1 => automatically reflects changes in l2
# If we make change using l2 => automatically reflects changes in l1

l1[1] = 7777
print(l1) # Output : [10, 7777, 30, 40]
print(id(l1)) # Output : 2757048055424

print(l2) # Output : [10, 7777, 30, 40]
print(id(l2)) # Output : 2757048055424

print(l1 is l2) # Output : True


# ------------------------------------------------------------------------------
# CLONING
# Process of creating completely different duplicate object, 
# not just duplicate reference variable is called cloning

#  Two ways to clone a list object :

# 1. using the slice() operator
# 2. using the copy() method
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 1. slice operator

l1 = [10, 20, 30, 40]

l2 = l1[::]

print(l1) # Output : [10, 20, 30, 40]
print(id(l1)) # Output : 2790298051200

print(l2) # Output : [10, 20, 30, 40]
print(id(l2)) # Output : 2790297645248



l1[1] = 7777
print(l1) # Output : [10, 7777, 30, 40]
print(id(l1)) # Output : 1603544965760

print(l2) # Output : [10, 20, 30, 40]
print(id(l2)) # Output : 1603544559808
# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
# 2. copy() method
l1 = [10, 20, 30, 40]

l2 = l1.copy()

print(l1) # Output : [10, 20, 30, 40]
print(id(l1)) # Output : 2180695373440

print(l2) # Output : [10, 20, 30, 40]
print(id(l2)) # Output : 2180697449088



l1[1] = 7777
print(l1) # Output : [10, 7777, 30, 40]
print(id(l1)) # Output : 2180695373440

print(l2) # Output : [10, 20, 30, 40]
print(id(l2)) # Output : 2180697449088
# ------------------------------------------------------------------------------