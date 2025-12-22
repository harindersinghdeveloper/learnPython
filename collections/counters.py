from collections import Counter
from itertools import count

#1 Counter on number list
my_number_list = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4]
print(Counter(my_number_list))

#2 Counter on string list
my_string_list = ['a','a','a','b','a','b','hello','hello','Hello','Hello','Canada','Faridkot','Faridkot']
print(Counter(my_string_list))

#3 Counter on a string
print(Counter('Harinder Singh Dhani'))

#4 Most common repetitions
print(Counter(my_number_list).most_common())
print(Counter(my_number_list).most_common(2))
