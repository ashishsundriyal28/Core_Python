# ==================================================================================================
#                                   IMPORTANT FUNCTIONS AND METHODS OF LIST
# ==================================================================================================

# -----------------------------------------------------------
# To get information about List:
# -----------------------------------------------------------

# 1. len() ==> Returns the number of elements present in the list
l = [10, 20, 30]
print(len(l))


# 2. count() ==> Returns the number of occurrences of specified element present in the list
l = [10, 20, 10, 20, 30, 20, 40]
print(l.count(10)) # Output : 2
print(l.count(20)) # Output : 3
print(l.count(50)) # Output : 0


# 3. index() ==> Returns index of the first occurrence of the specified item
l = [1, 2, 1, 2, 3, 4]
print(l.index(1)) # Output : 0
print(l.index(2)) # Output : 1
print(l.index(3)) # Output : 4

# Note : If the specified element not available then immediately we will get error.
# print(l.index(5)) # Output :  ValueError: list.index(x): x not in list


# l = [1, 2, 2, 2, 3, 3]

# x = int(input('Enter element to find: '))

# if x in l:
#     print('{} present at index:{}'.format(x, l.index(x)))
# else:
#     print(x, 'not available in list')



# -----------------------------------------------------------
# Manipulating elements of List:
# -----------------------------------------------------------

# 1. append() : add element at the end of the list

l = []

l.append(10)
l.append(20)
l.append(30)
print(l) # Output : [10, 20, 30]
l.append(40)
print(l) # Output : [10, 20, 30, 40]


# Add numbers which are divisible by 10 from 1 to 100

l = []

for x in range(1,101):
    if x%10==0:
        l.append(x)

print(l)



# 2. insert() : add element at a specific position of the list

# Syntax:
# l.insert(index, element)

l = [10, 20, 30, 40]
l.insert(1, 7777)
print(l) # Output : [10, 7777, 20, 30, 40]



# Python does NOT raise an IndexError when using insert().
# Instead, it handles invalid indexes intelligently.

# If specified index is: 
# greater than the max index => adds alements at last of the list
# less than the max index => adds alements in beginning of the list

l = [10, 20, 30, 40]
l.insert(100, 7777)
l.insert(-100, 9999)
print(l) # Output : [9999, 10, 20, 30, 40, 7777]