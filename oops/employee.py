class Employee:

    #CLASS OBJECT ATTRIBUTES
    #SAME FOR ANY INSTANCE OF A CLASS
    company = 'Google'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_details(self):
        print(f'Name: {self.name}')
        print(f'Salary: {self.salary}')
        print(f'Company: {self.company}')

