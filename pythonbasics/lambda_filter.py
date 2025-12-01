#mapFunction
def square(num):
    return num ** 2

print(list(map(square,list(range(10)))))

#filterFunction
def check_even(num):
    return num % 2 == 0
print(list(filter(check_even,list(range(10)))))

#lambdaExpression
myfunc = lambda num: num ** 2
print(list(map(myfunc,list(range(10)))))

print(list(filter(lambda num: num % 2 == 0, list(range(10)))))

