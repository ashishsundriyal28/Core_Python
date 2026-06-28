# --------------------------------------------------------------------------------------------------
# ---------- Creation of List Object -------------
# --------------------------------------------------------------------------------------------------

# 1. Create Empty list object

l = []
print(type(l)) # OUTPUT : <class 'list'>


# 2. If we knoe data already

l = [10, 20, 30, 40]
print(l)


# 3. Dynamic input

l = eval(input("Enter List : ")) # INPUT : [1,2,3]
print(type(l)) # OUTPUT : <class 'list'>


# 4. By using list function
# If we want to create and equivalent object or the given sequence, we can go for list

l = list('durga')
print(type(l)) # OUTPUT : <class 'list'>
print(l)


l = list(range(0,10,2))
print(type(l)) # OUTPUT : <class 'list'>
print(l) # OUTPUT : [0, 2, 4, 6, 8]



# 5. split() method of string returns list

s = "Learning Python is easy"
l = s.split()
print(l) # OUTPUT : ['Learning', 'Python', 'is', 'easy']