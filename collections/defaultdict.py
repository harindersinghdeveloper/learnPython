from collections import defaultdict

d = {'a': 2}
print(d['a'])
#print(d['b']) # here you would get an error because key 'b' doesn't exist in dictionary

# to handle above problem, you can use dafaultdict and assign a default value if key doesn't exist

d = defaultdict(lambda:0)
d['a'] = 1000
print(d['a'])
print(d['b'])