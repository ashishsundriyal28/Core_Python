# --------------------------------------------------------------------------------------------------
# ---------- Mathematical Operators for List -------------
# --------------------------------------------------------------------------------------------------

# ------------------------------------------------------------
# 1. Concatenation Operator (+)
# ------------------------------------------------------------
# We can concatenate two lists into a single list by using concatenation operator

l1 = [10, 20, 30]
l2 = [40, 50, 60]

l3 = l1+l2
print(l3) # Output : [10, 20, 30, 40, 50, 60]


# Note : If you want to use contenation operator for list make sure 
# both arguments should be list type only and not for other data type

# l1 = [10, 20, 30]
# l2 = l1+40
# print(l2) # Output : TypeError: can only concatenate list (not "int") to list

# l1 = [10, 20, 30]
# l2 = l1+(40. 50, 60)
# print(l2) # Output : TypeError: can only concatenate list (not "int") to list


l1 = [10, 20, 30]
l2 = l1+[40]
print(l2) # Output : [10, 20, 30, 40]



# ------------------------------------------------------------
# 2. Repetition Operator (*)
# ------------------------------------------------------------

# Note : Compulsory, One argument should be list, 
# and the other argument should be only *int* type, only then its applicable for the list

l1 = [10, 20]
l2 = l1*2
print(l2) # Output : [10, 20, 10, 20]


l1 = [10, 20]
l2 = [30, 40]
l3 = l1+l2
print(l3)  # Output : [10, 20, 30, 40]

l4 = l3*3
print(l4)  # Output : [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]