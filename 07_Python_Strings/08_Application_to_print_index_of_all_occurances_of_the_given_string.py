# --------------------------------------------------------------------------------------------------
# ---------- Application to find index of all occurances of the given substring -------------
# --------------------------------------------------------------------------------------------------

s = 'ABCABCABCA'

i = s.find('ABC')
print(i)

i = s.find('ABC',3,10)
print(i)

i = s.find('ABC',6,10)
print(i)

subs = 'ABC'
i=s.find(subs)
if i==-1:
    print('Specified SubString not found')

count=0
while i!=-1:
    count+=1
    print('{} present at index : {}'.format(subs,i))
    i = s.find(subs, i+len(subs), len(s))
print('Occurance : ', count)
# print('No. of occurances : ', s.count(subs))