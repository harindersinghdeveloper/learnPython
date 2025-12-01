class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        raise NotImplementedError()

class Dog(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,name,age)
    def speak(self):
        print(f'I am Dog, myname is {self.name} and my i am {self.age} years old. I say woof !!')
class Cat(Animal):
    def speak(self):
        print(f'I am Cat, myname is {self.name} and my i am {self.age} years old. I say meow !!')


d = Dog('Dog',20)
d.speak()
c = Cat('Cat',20)
c.speak()