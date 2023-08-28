# dunder methods
# special methods in python

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # __str__ used to print the object in the user friendly way.
    def __str__(self):
        return f"my name is {self.name} I am {self.age} years old and I am {self.gender}"
    
    # __add__ used to override the + operator
    def __add__(self, newperson):
        print("mutation is being performed")
        return Person(self.name, newperson.age, self.gender)
    
    # __eq__ comparator operator to compare 2 persons
    def __eq__(self, object):
        return self.age == object.age or self.name == object.name
    

one = Person("Karthik G k", 21, "Male")
print(one) # str method is called here

two = Person("SRK", 50, "Male")
three = one + two
print(three) # add operator is used

print(three == one)# equal to operator is used here
