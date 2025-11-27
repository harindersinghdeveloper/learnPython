def addnumbers(*args):
    return sum(args)
print(addnumbers(1, 2, 3))

def myFavFruit(**kwargs):
    print(kwargs)
    return kwargs['fruit']
def myFavVeggie(**kwargs):
    return kwargs['vegetable']

print(myFavFruit(fruit='apple', vegetable='banana'))
print(myFavVeggie(fruit='apple', vegetable='banana'))

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    return args[0] + kwargs['amount']

print(myfunc(1, 2, 3,moneyin='$',amount=300))