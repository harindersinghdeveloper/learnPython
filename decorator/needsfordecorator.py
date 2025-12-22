#assigning a function to a variable

def hello():
    return "Hello World"

greetings = hello()
print(greetings)

#returning a function

def hellonew():
    print("i am inside hellonew")
    def greet():
        return "hello world"
    return greet()

print(hellonew())

#passing a function as an argument

def new_Greetings(some_function):
    print("i am inside new_Greetings")
    print(some_function())

new_Greetings(hello)
