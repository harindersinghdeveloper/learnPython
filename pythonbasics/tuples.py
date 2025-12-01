#Tuples are immutable - once element is inside a tuple, it cannot be reassigned

my_tuple = (1, 2, 3)
another_tuple = (4, 5, 6,4)
print(my_tuple)
print(another_tuple)
print(my_tuple + another_tuple)
print(another_tuple.count(4))
print(another_tuple.index(4))

