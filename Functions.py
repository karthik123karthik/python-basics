# passing arguements into a function

def default_function(name, age=20):
    print(name , age)

default_function("karthik", 21)
default_function("karthik")

def variable_arguements(*args):
    print(args)

variable_arguements([1,2,3,4])
variable_arguements(1,2,3, 4)

def variable_arguements_maps(**kwargs):
    print(kwargs)

variable_arguements_maps(name =1, age=20, val=50)



