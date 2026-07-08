# ==================================================================================================
#                    LIST COMPREHENSION
# ==================================================================================================


# --------------------------------------------------------------------------------------------------
# WHAT IS LIST COMPREHENSION?
# --------------------------------------------------------------------------------------------------
# List Comprehension is a short and Pythonic way to create a new list.
#
# It replaces:
#
#   1. Create an empty list
#   2. Iterate using a loop
#   3. Apply some operation (optional)
#   4. Append each result
#
# with a single readable line of code.
#
# It is:
# ✔ Shorter
# ✔ Cleaner
# ✔ Faster than using append() inside a loop (in most cases)
# ✔ Preferred Python style

# --------------------------------------------------------------------------------------------------
# GENERAL SYNTAX
# --------------------------------------------------------------------------------------------------


l=[]
for i in range(1,11):
    l.append(i)

print(l) # Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ----------------------------
# List Comprehension Way
# ----------------------------

# Syntax : 

# Without condition
# [expression for each_element in sequence]

# With condition
# [expression for each_element in sequence if condition]

# --------------------------------------------------------------------------------------------------
# HOW TO READ A LIST COMPREHENSION
# --------------------------------------------------------------------------------------------------

# Example:
#
# [x*x for x in range(1,11)]
#
# Read it from RIGHT to LEFT:
#
# Step 1:
# Take every x from range(1,11)
#
# Step 2:
# Evaluate x
#
# Step 3:
# Store every result inside a new list

l = [x for x in range(1,11)]
print(l) # Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# --------------------------------------------------------------------------------------------------
# BREAKDOWN OF COMPONENTS
# --------------------------------------------------------------------------------------------------

# [ expression      for variable     in iterable      if condition ]
#      │                 │                │                  │
#      │                 │                │                  │
#      │                 │                │                  └── Optional filtering
#      │                 │                │
#      │                 │                └── Data source
#      │                 │
#      │                 └── Current element
#      │
#      └── What should be stored in the list


# --------------------------------------------------------------------------------------------------
# NORMAL LOOP VS LIST COMPREHENSION
# --------------------------------------------------------------------------------------------------

# Normal Loop
#
# result = []
# for x in iterable:
#     result.append(expression)
#
# List Comprehension
#
# result = [expression for x in iterable]


# Example : Creation of list with square values of numbers from 1 to 10

l = [x*x for x in range(1,11)]
print(l) #Output : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Example : Creation of list with values of power of 2 from 1 to 10

l = [2**x for x in range(1,11)]
print(l) # Output : [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]


# Example : Creation of list with numbers from 1 to 100 which are divisible by 10

l = [x for x in range(1,101) if x%10==0]
print(l) # Output : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# **Example : Creation of list with elements present in l1 but not in l2

l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]

l3 = [x for x in l1 if x not in l2]
print(l3) # Output : [10, 20] 


# **Example : Creation of list with elements present in both l1 and l2

l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]

l3 = [x for x in l1 if x in l2]
print(l3) # Output : [30, 40] 


# ------------------------
# STRING EXAMPLES
# ------------------------
# **Example : Creation of list with only first characters of each word in list

l = ["Harjot", "Balaiah", "NagaArjun", "Venkat", "Jignesh"]
l1 = [word[0] for word in l]
print(l1) # Output : ['H', 'B', 'N', 'V', 'J']



# **Example : Want to create a nested list where every individual word is itself 
# a list (inside one bigger list) with its length as its second element

s = 'The quick brown fox jumps over the lazy dog'

words = s.split()
print(words)  # Output : ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


l = [[word.upper(), len(word)] for word in words]
print(l) # Output : [['THE', 3], ['QUICK', 5], ['BROWN', 5], ['FOX', 3], ['JUMPS', 5], ['OVER', 4], ['THE', 3], ['LAZY', 4], ['DOG', 3]]





# -----------------------------------------------------------------------------------
# Program to display unique vowels present in the given word?
# -----------------------------------------------------------------------------------


vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter any string : ')
result = []

# WAY 1
# for ch in word:
#     if ch in vowels:
#         if ch not in result : 
#             result.append(ch)

# WAY 2
for ch in vowels:
    if ch in word:
        result.append(ch)

# WAY 3 (same as Way 2 but list-comprehension way)
results = [ch for ch in vowels if ch in word]

print(result)
print("The no of unique vowels : ", len(result))

print(results)
print("The no of unique vowels results : ", len(results))

# Why?

# Because every vowel is checked only once.
# Therefore, duplicate vowels automatically disappear.

# Example:
#
# word = "banana"
#
# Checks:
#
# a ✔
# e ✘
# i ✘
# o ✘
# u ✘
#
# Result:
#
# ['a']
#
# even though 'a' occurs multiple times.


# --------------------------------------------------------------------------------------------------
# WHEN TO USE LIST COMPREHENSION
# --------------------------------------------------------------------------------------------------

# Use it when:
#
# ✔ Creating a new list
# ✔ Applying an operation to every element
# ✔ Filtering elements
# ✔ Mapping one list into another
#
# Examples:
#
# Squares
# Cubes
# Uppercase strings
# Even numbers
# First characters
# Common elements
# Unique values
# Nested lists


# --------------------------------------------------------------------------------------------------
# WHEN NOT TO USE LIST COMPREHENSION
# --------------------------------------------------------------------------------------------------

# Avoid it when:
#
# ✘ Logic is very complicated
# ✘ Multiple nested loops reduce readability
# ✘ Many if-else blocks make it confusing
#
# In such cases,
# a normal for-loop is easier to understand.


# --------------------------------------------------------------------------------------------------
# ADVANTAGES
# --------------------------------------------------------------------------------------------------

# ✔ Less code
# ✔ More readable
# ✔ Faster execution (generally)
# ✔ Pythonic
# ✔ Easy to write mapping and filtering logic