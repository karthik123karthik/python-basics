# poly means many and morphism means forms
# duck typing

class Laptop:

    def code(self, ide):
        ide.execute()  # pyhton only focus on execute func

class Pycharm:

    def execute(self):
        print("Compiling the program")
        print("Running the program")

class Vscode:

    def execute(self):
        print("Running the code")
        print("printing the output")


ide = Pycharm()
l1 = Laptop()
l1.code(ide)

# operator overloading

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __str__(self):
        return f'{self.m1} {self.m2}'
    
    def __add__(self, other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        s3 = Student(r1,r2)
        return s3




s1 = Student(10, 20)
s2 = Student(30, 40)
print(s1)  # override the print operator
print(s1 + s2)  # Student.__add__(s1,s2)

# there is no method overloading in python