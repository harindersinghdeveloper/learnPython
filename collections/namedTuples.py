from collections import namedtuple

# main benefit of named tuple is that you can also fetch by key, not just index
# still behaves like tuple
# immutable(safe from accidental changes)

User = namedtuple('user', ['name','age','salary'])

user1 = User('John', '25', 20000)
print(user1.name)
print(user1[0])
print(user1.age)
print(user1[1])
print(user1.salary)
print(user1[2])