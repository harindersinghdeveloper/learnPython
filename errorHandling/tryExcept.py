def add(a,b):
    try:
        return a+b
    except:
        print("error while adding your numbers")
        return 0

print(add(2,3))
print("I am running after addition") # as now, we have handled error now this code will run