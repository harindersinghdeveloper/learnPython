def add(*args):
    var1 = 0
    for arg in args:
        var1 += arg
    return var1

def multiply(*args):
    var1 = 1
    for arg in args:
        var1 = arg * var1
    return var1

if __name__ == '__main__':
    print(f'add function works fine : {add(2,2)==4}')