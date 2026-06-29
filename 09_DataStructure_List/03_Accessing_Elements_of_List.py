# --------------------------------------------------------------------------------------------------
# ---------- Accessing Elements of List -------------
# --------------------------------------------------------------------------------------------------

# 1. By using index
l = [10, 20, 30, 40]

# print(l[0]) # OUTPUT : 10
# print(l[-1]) # OUTPUT : 40
# print(l[100]) # OUTPUT : IndexError


# 2. By using slice operator

# list = l[begin:end:step]

# If step is +ve => Forward Direction => begin to end-1
# If step is -ve => Backward Direction => begin to end+1

# Note
# In forward direction => If end value is 0 => then result is always empty
# In backward direction => If end value is -1 => then result is always empty

# -----------------------------------------------------------------------------
# Either forward direction or backward direction, we can
# take both +ve and -ve values for begin and end index

# In forward direction:
# default value for begin: 0
# default value for end: len(list)

# In backward direction:
# default value for begin: -1
# default value for end :- (len(list)+1)
# -----------------------------------------------------------------------------


l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Forward Index (Left → Right)
#
#          0    1    2    3    4    5    6    7    8     9
#        ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬─────┐
# l    = │ 10 │ 20 │ 30 │ 40 │ 50 │ 60 │ 70 │ 80 │ 90 │ 100 │
#        └────┴────┴────┴────┴────┴────┴────┴────┴────┴─────┘
#         -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
#
# Backward Index (Right → Left)


# From 2nd index to 6th index (7th index is excluded)
print(l[2:7])               # Output: [30, 40, 50, 60, 70]

# From 2nd index to 6th index, taking every 2nd element
print(l[2:7:2])             # Output: [30, 50, 70]

# From 4th index to the end, taking every 2nd element
print(l[4::2])              # Output: [50, 70, 90]

# From 8th index to 3rd index (exclusive), moving backwards by 2
print(l[8:2:-2])            # Output: [90, 70, 50]

# From 4th index to the end (stop index is beyond the list length)
print(l[4:100])             # Output: [50, 60, 70, 80, 90, 100]

# From 4th index to 0th index, moving forward by 2 (invalid slice direction)
print(l[4:0:2])             # Output: []


print(l[::1])             # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(l[::-1])            # Output: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
