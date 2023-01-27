#setters and getters in python

class Example:
    def __init__(self,value):
        self.value = value
    
    # getter is used to convert a method to a property of the class
    @property #it is used to specify that it is a getter
    def get_value(self):
        print(self.value)
    
    @get_value.setter # as name says it is used to set the value.
    def set_value(self,newvalue):
        self.value = newvalue


one = Example(20)
one.get_value
one.set_value = 10
one.get_value
