# ==================================================================================================
#                                   IMPORTANT FUNCTIONS OF LIST
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# 1. len()
# --------------------------------------------------------------------------------------------------
# Returns the total number of elements present in the list.
#
# Syntax:
# len(list_name)
#
# It counts every element only once, regardless of duplicates.

l = [10, 20, 30]
print(len(l))          # Output: 3


# --------------------------------------------------------------------------------------------------
# 2. count()
# --------------------------------------------------------------------------------------------------
# Returns how many times a specified element appears in the list.
#
# Syntax:
# list_name.count(element)
#
# If the element does not exist, it returns 0.
# It NEVER raises an error.

l = [10, 20, 10, 20, 30, 20, 40]

print(l.count(10))     # Output: 2
print(l.count(20))     # Output: 3
print(l.count(50))     # Output: 0


# --------------------------------------------------------------------------------------------------
# 3. index()
# --------------------------------------------------------------------------------------------------
# Returns the index of the FIRST occurrence of the specified element.
#
# Syntax:
# list_name.index(element)
#
# Important:
# If the element appears multiple times,
# only the first occurrence is returned.

l = [1, 2, 1, 2, 3, 4]

print(l.index(1))      # Output: 0
print(l.index(2))      # Output: 1
print(l.index(3))      # Output: 4

# Remember:
# If the element does NOT exist,
# Python raises:
#
# ValueError: list.index(x): x not in list
#
# Therefore, it is a good practice to check first.

# l = [1, 2, 2, 2, 3, 3]
# x = int(input('Enter element to find: '))
# if x in l:
#     print(l.index(x))
# else:
#     print("Element not found")


# ==================================================================================================
#                              ADDING (INSERTING) ELEMENTS
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# 1. append()
# --------------------------------------------------------------------------------------------------
# Adds ONE element to the END of the list.
#
# Syntax:
# list_name.append(element)
#
# Important:
# append() always adds only ONE object.
#
# If that object is another list,
# the entire list becomes ONE element.

l = []

l.append(10)
l.append(20)
l.append(30)

print(l)

l.append(40)

print(l)


# Example:
# Store numbers divisible by 10 from 1 to 100.

l = []

for x in range(1, 101):
    if x % 10 == 0:
        l.append(x)

print(l)


# --------------------------------------------------------------------------------------------------
# 2. insert()
# --------------------------------------------------------------------------------------------------
# Inserts an element at a specified index.
#
# Syntax:
# list_name.insert(index, element)

l = [10, 20, 30, 40]

l.insert(1, 7777)

print(l)

# Python does NOT raise an IndexError when using insert().
# Instead, it handles invalid indexes intelligently.

# If specified index is: 
# greater than the max index => adds alements at last of the list
# less than the max index => adds alements in beginning of the list

l = [10, 20, 30, 40]
l.insert(100, 7777)
l.insert(-100, 9999)
print(l) # Output : [9999, 10, 20, 30, 40, 7777]


# --------------------------------------------------------------------------------------------------
# 3. extend()
# --------------------------------------------------------------------------------------------------
# Used to add all elements from another iterable
# (list, tuple, string, set, etc.)
#
# Syntax:
# list1.extend(iterable)
#
# Every element is added individually.

order1 = ["Chicken", "Mutton", "Fish"]
order2 = ["KF", "KO", "RC"]

order1.extend(order2)

print(order1)


# ==================================================================================================
#                        append() vs extend()
# ==================================================================================================

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


# l1.extend('ABC')
# print(l1) # Output : [10, 20, 30, 'A', 'B', 'C']
# print(len(l1)) # Output : 6


print("-" * 70)


print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

# ==================================================================================================
#                                 REMOVING ELEMENTS
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# 1. remove()
# --------------------------------------------------------------------------------------------------
# => removes the first occurance of the specified element from the list
# => if the specified element is not present in the list, it raises a ValueError

# Syntax:
# list_name.remove(element)

# Important: It removes by VALUE, not by INDEX.

l = [10, 20, 10, 20, 40]
l.remove(10)
print(l) # Output : [20, 10, 20, 40]
# removed the first occurance of 10 from the list

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
print("--------------------- SMALL EXERCISE ----------------------")
print("-----------------------------------------------------------")

# HOW TO REMOVE ALL OCCURANCES OF SPECIFIED ELEMENT FROM THE LIST

# => Ready-made methods not available, have to write code

# l = [1, 1, 1, 1, 2, 2, 2, 3, 3]
# print('Before Removal:', l)
# x = int(input('Enter element to remove: '))

# while True:
#     if x in l:
#         l.remove(x)
#     else:
#         break
# print('After Removal:', l)


# --------------------------------------------------------------------------------------------------
# 2. pop()
# --------------------------------------------------------------------------------------------------
# Removes AND RETURNS an element.

# --------------------------------------------
# i. pop() 
# --------------------------------------------
# Without an argument:
# Removes the LAST element.

# Syntax : l.pop()

l = [10, 20, 30]
print(l.pop()) # Output : 30
print(l) # Output : [10, 20]

# ----------------------------------------------------------------------------------------
# Note : If the list is empty and we try to pop an element, then we will get IndexError.

# l = []
# print(l.pop()) # Output : IndexError: pop from empty list
# ----------------------------------------------------------------------------------------


# --------------------------------------------
# ii. pop(index) 
# --------------------------------------------
# with an argument
# removes and returns the element present at the specified index

# Syntax : l.pop(index)


l = [10, 20, 30, 40]
print(l.pop(1)) # Output : 20
print(l) # Output : [10, 30, 40]

# print(l.pop(100)) # Output : IndexError: pop index out of range


'''
+---------------------------------------------------------------------------------------------------------------+
|                     Differences between remove() and pop() in Python                                          |
+------------------------------+------------------------------------------------+-------------------------------+
|           remove()           |                    Description                 |            pop()              |
+------------------------------+------------------------------------------------+-------------------------------+
| Syntax                       | list.remove(x)                                 | list.pop()                    |
|                              | Removes the specified element                  | Removes & returns last item   |
|                              |                                                |                               |
|                              |                                                | list.pop(index)               |
|                              |                                                | Removes & returns element     |
|                              |                                                | at specified index            |
+------------------------------+------------------------------------------------+-------------------------------+
| Empty List                   | Raises ValueError                              | Raises IndexError             |
+------------------------------+------------------------------------------------+-------------------------------+
| Return Value                 | Returns None                                   | Returns the removed element   |
+------------------------------+------------------------------------------------+-------------------------------+
'''

# --------------------------------------------------------------------------------------------------
# 3. clear()
# --------------------------------------------------------------------------------------------------
# removes all the elements present inside the list 

l = [10, 20, 30, 40]
l.clear()
print(l) # Output : []