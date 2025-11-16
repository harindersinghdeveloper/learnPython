var1 = "hello"

print(var1)

#Indexing of string
print(var1[1])
print(var1[-1]) # last char in string
print(len(var1))

#Slicing of string
print(var1[2:])
print(var1[:3])
print(var1[2:4])
print(var1[-4:-1])

#Step size
print(var1[1:4:2])
print(var1[::-1])

#String properties and methods
#immutable
name = "Sam is here"

print(name.upper())
print(name.lower())
print(name.split())
print(name.split('is'))

#Formatting

message = "Hello {}, Good Morning, Today is {} !!"

print(message.format("Sam", "Sunday"))

print("My days are {} {} {}".format("Sunday", "Monday", "Tuesday"))
print("My days are {0} {0} {0}".format("Sunday", "Monday", "Tuesday"))
print("My days are {s} {m} {t}".format(s="Sunday", m="Monday", t="Tuesday"))

#Formatting with string literals
print(f'Hello , his name is {name}')