# --------------------------------------------------------------------------------------------------
# ---------- Accessing Elements of List -------------
# --------------------------------------------------------------------------------------------------


# Forward Index (Left → Right)
#
#          0    1    2    3    4    5    6    7    8    9    10
#        ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
# l    = │ 0  │ 1  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │ 9  │ 10 │
#        └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
#        -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
#
# Backward Index (Right → Left)
#
#
# Index :  0    1    2    3    4    5    6    7    8    9    10
# Value :  0    1    2    3    4    5    6    7    8    9    10
# Index : -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. By using while loop:
# i = 0
# while i<len(l):
#     print(l[i])
#     i+=1


# 2. By using for loop:

# for x in l:
#     print(x)


# 3. To print only even numbers:

# for x in l:
#     if x%2==0:
#         print(x)


# 4. Print elements ofr list index-wise

l = [10, 20, 30, 40, 50, 60]

# Note : Rule to get negative index
# -ve index = +ve index - length_of_list

i = 0
while i < len(l):
    print(
        "The element present at +ve index : {} and at -ve index : {} is : {}".format(
            i, i - len(l), l[i]
        )
    )
    i += 1

# Even better (using f-strings)

i = 0
while i < len(l):
    print(f"The element present at +ve index : {i} and at -ve index : {i - len(l)} is : {l[i]}")
    i += 1