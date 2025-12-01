class Book:
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages

    #dunder/magic methods
    def __str__(self):
        return f'Book Name: {self.name}, Author: {self.author}'

    def __len__(self):
        return self.pages

b = Book("Dark", "Harinder",300)

print(b) #this will print <__main__.Book object at 0x0000024F6C296F90> we have to override string method to print correct information of the book, those are known as magic/dunder methods
print(len(b))