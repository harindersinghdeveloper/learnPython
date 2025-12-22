import timeit

def my_list(n):
    return list(str(num) for num in range(n))
print(my_list(5))

def my_list_one(n):
    return list(map(str,range(n)))
print(my_list_one(5))

stmt = '''
my_list(100)
'''
setup ='''
def my_list(n):
    return list(str(num) for num in range(n))
'''


stmt_one = '''
my_list_one(100)
'''
setup_one ='''
def my_list_one(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt, setup, number=100000))
print(timeit.timeit(stmt_one, setup_one, number=100000))