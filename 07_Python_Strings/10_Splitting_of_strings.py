# --------------------------------------------------------------------------------------------------
# ---------- Spliting of strings -------------
# --------------------------------------------------------------------------------------------------

# SYNTAX: 
# string.split(separator, maxsplit)
# default separator is space and default maxsplit is -1 which means all occurances

# return type is always list

s = "Durga Software solutions"
l = s.split()
print(l) # Output : ['Durga', 'Software', 'solutions']

# fetch
for x in l:
    print(x)

# OUTPUT : 
# Durga
# Software
# solutions


d = '05-04-2019'
l = d.split('-')
print(l) # OUTPUT : ['05', '04', '2019']

# fetch
for x in l:
    print(x)

# OUTPUT : 
# 05
# 04
# 2019



# --------------------------------------------------------------------------------------------------
# ---------- Joining of strings -------------
# --------------------------------------------------------------------------------------------------

# SYNTAX: 
# separator.join(list_of_strings)


l = ['Durga', 'Software', 'Solutions']
s = " ".join(l)
print(s) # OUTPUT : Durga Software Solutions


s = "-".join(l)
print(s) # OUTPUT : Durga-Software-Solutions

l = ['05', '04', '2019']
s = "-".join(l)
print(s) # OUTPUT : 05-04-2019