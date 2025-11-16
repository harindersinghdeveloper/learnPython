my_list = [1,2,3]
another_list = [4,"Five","Mango",2.44]
print(my_list)
print(len(my_list))
#indexing
print(my_list[-1])
#slicing
print(my_list[1:])
#merging list
print(my_list+another_list)
#update list
my_list[0]="One"
print(my_list)
#methods
my_list.append(6)
print(my_list)
popped_item = my_list.pop()
print(my_list)
print(popped_item)
indexed_popped_item = my_list.pop(1)
print(my_list)
print(indexed_popped_item)
