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


# 3. extend() : To add all elements of given sequence to the list

# Syntax : 
# l1.extend(l2)

# all elements present inside l2 will be added to the end of l1


order1 = ['Chicken', 'Mutton', 'Fish']
order2 = ['KF', 'KO', 'RC']

order1.extend(order2)
print(order1) # Output : ['Chicken', 'Mutton', 'Fish', 'KF', 'KO', 'RC']


# -----------------------------------------------------------

# Difference between append() and extend() : 

l1 = [10, 20, 30]
l2 = [40, 50]

# append() : adds the entire list as a single element to the end of the list
# l1.append(l2)
# print(l1) # Output : [10, 20, 30, [40, 50]]
# print(len(l1)) # Output : 4

# l1.append('ABC')
# print(l1) # Output : [10, 20, 30, 'ABC']
# print(len(l1)) # Output : 4

# extend() : adds all elements of the list to the end of the list
# l1.extend(l2)
# print(l1) # Output : [10, 20, 30, 40, 50]
# print(len(l1)) # Output : 5


l1.extend('ABC')
print(l1) # Output : [10, 20, 30, 'A', 'B', 'C']
print(len(l1)) # Output : 6


print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
# -----------------------------------------------------------
# Removing elements from List:
# -----------------------------------------------------------

# 1. remove() : 
# => removes the first occurance of the specified element from the list
# => if the specified element is not present in the list, it raises a ValueError

l = [10, 20, 10, 20, 40]
l.remove(10)
print(l) # Output : [20, 10, 20, 40]
#  removed the first occurance of 10 from the list

# l.remove(50)
# print(l) # Output : ValueError: list.remove(x): x not in list

print("-----------------------------------------------------------")
print("--------------------- SMALL EXERCISE ----------------------")
print("-----------------------------------------------------------")

# l = [1, 2, 3, 4, 5]
# print('Before Removal:', l)
# x = int(input('Enter element to remove: '))
# if x in l:
#     l.remove(x)
#     print('After Removal:', l)
# else:
#     print(x, 'not present in list')



print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

# HOW TO REMOVE ALL OCCURANCES OF SPECIFIED ELEMENT FROM THE LIST

# => Ready-made methods not available, have to write code

l = [1, 1, 1, 1, 2, 2, 2, 3, 3]
print('Before Removal:', l)
x = int(input('Enter element to remove: '))

while True:
    if x in l:
        l.remove(x)
    else:
        break
print('After Removal:', l)