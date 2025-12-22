# this is storing the entire list in the memory. but in most cases we needed one value at a time

def create_cube(n):
    return list(x**3 for x in range(n))
print(create_cube(10))

# here generators come into picture.
#generator
def create_cube(n):
    for y in range(n):
        yield y**3

#for z in create_cube(10):
#    print(z)
#generate one at a time on calling, more memory efficient
gen = create_cube(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
