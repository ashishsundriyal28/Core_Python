# ==================================================================================================
#                                Accessing Elements of TUPLE
# ==================================================================================================

# There are two ways to access tuple elements:
#   1. Indexing        -> Access a single element
#   2. Slicing         -> Access multiple elements (returns a new tuple)


# ==================================================================================================
# 1. ACCESSING ELEMENTS USING INDEX
# ==================================================================================================

t = (10, 20, 30, 40, 50, 60)

# Positive Indexing (Left ➜ Right)
# Index starts from 0.

#      0   1   2   3   4   5
# t = (10, 20, 30, 40, 50, 60)

print(t[0])      # Output: 10
print(t[1])      # Output: 20
print(t[5])      # Output: 60


# Negative Indexing (Right ➜ Left)
# Index starts from -1.

#     -6  -5  -4  -3  -2  -1
# t = (10, 20, 30, 40, 50, 60)

print(t[-1])     # Output: 60
print(t[-2])     # Output: 50
print(t[-6])     # Output: 10


# Invalid Index
# Accessing an index outside the tuple size raises IndexError.

# print(t[100])     # IndexError: tuple index out of range
# print(t[-100])    # IndexError: tuple index out of range


# ==================================================================================================
# 2. ACCESSING ELEMENTS USING SLICING
# ==================================================================================================

# Syntax: 
# tuple[begin:end:step]

# Slicing ALWAYS returns a NEW tuple.
# Original tuple remains unchanged.

t = (10, 20, 30, 40, 50, 60, 70, 80)

# Index Position
#
#          0   1   2   3   4   5   6   7
# t =    (10, 20, 30, 40, 50, 60, 70, 80)
#         -8  -7  -6  -5  -4  -3  -2  -1

# --------------------------------------------------------------------------------------------------
# Understanding start, end and step
# --------------------------------------------------------------------------------------------------

# start -> Starting index (Included)
# end   -> Ending index (Excluded)
# step  -> Number of positions to move each time

# Remember:
# -> start is INCLUDED
# -> end is EXCLUDED


# Example:
print(t[2:5])          # Output: (30, 40, 50)
# Starts from index 2
# Stops before index 5

# --------------------------------------------------------------------------------------------------
# STEP VALUE
# --------------------------------------------------------------------------------------------------

# step can be:
#   Positive (+ve)
#   Negative (-ve)


# ==============================================================================================
# A. Positive Step (Left ➜ Right)
# ==============================================================================================

# Moves from Left to Right.

print(t[::2])          # Output: (10, 30, 50, 70)
print(t[1::2])         # Output: (20, 40, 60, 80)
print(t[2:7:2])        # Output: (30, 50, 70)

# Direction:
# Left  -------------------------------------------------> Right


# Default Values (Positive Step)
#
# start = 0
# end   = len(tuple)
# step  = 1

print(t[:])            # Output: (10, 20, 30, 40, 50, 60, 70, 80)
print(t[:5])           # Output: (10, 20, 30, 40, 50)
print(t[3:])           # Output: (40, 50, 60, 70, 80)

# ==============================================================================================
# B. Negative Step (Right ➜ Left)
# ==============================================================================================

# Moves from Right to Left.

print(t[::-1])         # Output: (80, 70, 60, 50, 40, 30, 20, 10)
print(t[::-2])         # Output: (80, 60, 40, 20)
print(t[6:2:-1])       # Output: (70, 60, 50, 40)

# Direction:
# Right <------------------------------------------------- Left


# Default Values (Negative Step)
#
# start = -1
# end   = -(len(tuple) + 1)
# step  = -1

print(t[::-1])         # Reverse tuple


# ==================================================================================================
# IMPORTANT RULES OF SLICING
# ==================================================================================================

# Rule 1:
# Positive step  -> Traverses Left to Right

print(t[2:6])          # (30, 40, 50, 60)


# Rule 2:
# Negative step -> Traverses Right to Left

print(t[6:2:-1])       # (70, 60, 50, 40)


# Rule 3:
# End index is NEVER included.

print(t[1:4])          # (20, 30, 40)
# Index 4 (50) is excluded.


# Rule 4:
# If start and end do not match the traversal direction,
# result will be an empty tuple.

print(t[5:2])          # ()
# Positive step tries moving left ➜ right.
# But start > end, so nothing is returned.

print(t[2:5:-1])       # ()
# Negative step tries moving right ➜ left.
# But start < end, so nothing is returned.


# Rule 5:
# In forward direction, if end = 0
# result is always empty.

print(t[2:0])          # ()


# Rule 6:
# In backward direction, if end = -1
# result is always empty.

print(t[5:-1:-1])      # ()


# ==================================================================================================
# USING NEGATIVE INDICES
# ==================================================================================================

print(t[-5:-2])        # (40, 50, 60)
print(t[-2:])          # (70, 80)
print(t[:-3])          # (10, 20, 30, 40, 50)


# Negative indices can be mixed with positive indices.

print(t[2:-2])         # (30, 40, 50, 60)
print(t[-6:6])         # (30, 40, 50, 60)


# ==================================================================================================
# COPYING A TUPLE
# ==================================================================================================

# Slicing can be used to create a copy.

copy_tuple = t[:]

print(copy_tuple)
# Output: (10, 20, 30, 40, 50, 60, 70, 80)


# ==================================================================================================
# REVERSING A TUPLE
# ==================================================================================================

reverse_tuple = t[::-1]

print(reverse_tuple)
# Output: (80, 70, 60, 50, 40, 30, 20, 10)