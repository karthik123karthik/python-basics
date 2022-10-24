#create a class
class Computer:
    #constructor
    electronic_device = True # static variables
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self.cpu, self.ram)

    @classmethod
    def get_info(cls):
        return cls.electronic_device
    
    @staticmethod
    def say_hi():
        print("hello world")
    
    # instant variable and static variable
    # static variable are common for all the objects

 
    def compare(self, other):
        if self.cpu == other.cpu:
            return True
        else:
            return False            

comp1 = Computer("i5",16)
# print(type(comp1))
comp1.config()
print(id(comp1))  #address of comp1 object

# comparing two objects
comp2 = Computer("i3",4)
print(Computer.electronic_device)
comp2.electronic_device = False  # donot change static value 
print(comp2.electronic_device)
if comp2.compare(comp1):
    print("they are same")
else:
    print("they are different")

# different types of methods static methods, instance methods, class method 
print(comp1.get_info())
comp2.say_hi()



