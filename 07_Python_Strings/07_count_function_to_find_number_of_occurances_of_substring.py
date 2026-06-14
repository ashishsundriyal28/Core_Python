# --------------------------------------------------------------------------------------------------
# ---------- String Methods : count() -------------
# --------------------------------------------------------------------------------------------------

# Counting of substrings 

# 1. s.count(substring):
# returns the number of occurrences of the given substring in the total string  

# 2. s.count(substring,begin,end):
# returns the number of occurrences of the given substring from begin index to end-1 index

s = 'ABBABBABA'

# count() method : 
# returns the number of non-overlapping occurrences of the substring in the string
print(s.count('B'))  # Output: 5
print(s.count('A'))  # Output: 4
print(s.count('C'))  # Output: 0

# can also use it in a specific range
# also, upper limit can be grearter than the last index of the string
# it will automatically read until the last index only
print(s.count('B', 4, 100))  # Output: 3



# can also work on multiple characters as substring

s = 'BBBBB'

print(s.count('B'))  # Output: 5
print(s.count('BB'))  # Output: 2
print(s.count('BBB'))  # Output: 1