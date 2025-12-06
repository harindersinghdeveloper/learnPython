try:
    f = open("test.txt","r")
    f.write("Hello World")
except TypeError as e:
    print("I am type error")
    print(e)
except OSError as e:
    print("I am OS error")
    print(e)
finally:
    print("I am running after finally")

