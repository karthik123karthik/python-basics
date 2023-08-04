class Employee:
     #this is called magic/dunder method and is used to do some crazy things
      def __str__(self):
          return "this is employee class"

      def __add__(self, b):
           return "added"


e1= Employee()
print(e1)
