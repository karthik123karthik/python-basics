
# functions are used for code reusability
def greet(name, place):
     print(f'hello {name} welcome {place}')

greet("karthik", "home")

# write a function that take the parameters of variable length and prints it

def func(*input):
     print(input)

func([1,2,3,4]);
