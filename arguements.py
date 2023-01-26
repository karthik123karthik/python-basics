# arguements of a function in python
# 1. required arguements
# 2. default arguements
# 3. key arguements
# 4. using * as aguements
# 5. ** for dictionary as arguements

#1.required arguements
def greet(first_name, last_name):
     print(f'hello {first_name} {last_name}')

greet("karthik","G K")

# 2.default arguements
def greet(first_name,last_name="G K"):
     print(f'hello {first_name} {last_name}')

greet("karthik","g k")

# 3.key arguements
def volume(length, height, width):
     print(length,height,width)
     print(length*height*width)

volume(length=20,width=10,height=30)

# 4.using * which will consider all arguements as tuple

def volume(*sides):
     print(sides[0]*sides[1]*sides[2])

volume(20,10,30)
vol = [20,10,30]
volume(*vol)

# 5.using double star will consider all arguements as dictionary

def volume(**sides):
     print(sides['length']*sides['width']*sides['height'])

volume(length = 20,height = 10, width = 30)


