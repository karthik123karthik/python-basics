# python donot have concept of private and protected we use it as a convention.

class Employe:
      def __init__(self):
           self.__name = "karthik" # way to define a private variable
           self._name = "karthik" # way to define a protected variable

emp = Employe()
print(emp._Employe__name) #accesing a private variable
print(emp._name) #accesing a protected variable.
