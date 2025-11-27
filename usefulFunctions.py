mylist  = list(range(0,100,2))
print(mylist)

line = 'i love canada'
print(line)
for l in enumerate(line):
    print(l)
for i,l in enumerate(line):
    print(i,l)

list1 = list(range(5))
list2 = ['a','b','c','d','e','f','g']
print(list1)
print(list2)

for list3 in zip(list1,list2):
    print(list3)

print('c' in list2)

