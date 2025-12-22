import time
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
    def wrapper(*args, **kwargs):
        print(f'Calling function: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

def logTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        myfunc = func(*args, **kwargs)
        end = time.time()
        print(f'Function "{func.__name__}" took {end - start:.10f} seconds')
        return myfunc
    return wrapper

@log
@logTime
def say_hello():
    for i in range(2):
        print('Hello')

@log
@logTime
def add_numbers(a,b):
    return a+b

say_hello()
print(add_numbers(1,2))