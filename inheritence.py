# single level inheritence
class Car:
    def __init__(self):
        print("It belongs to four wheeler category")
    

class Tesla(Car):
    def __init__(self):
        super().__init__()
        print("manufactored by tesla company")



# multilevel inheritence
class Teslamodal1(Tesla):
        def __init__(self):
             super().__init__()
             print("It is a new model of tesla")
    
# multiple inheritence
class Flight:
    def __init__(self):
        print("It can fly")

class Teslamodel2(Flight, Tesla): # follows MRO i,e left has high priority
    def __init__(self):
         super().__init__()

car1 = Teslamodel2()

# hybrid is nothing but both multilevel and multiple
