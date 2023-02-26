# generators in python
# they will give the sequence value at the fly time
# they are very powerful to handle large data
# there is no need to store data
# it  will yeild us the ingredients to make data at any given instance 

def generator_func():
    #yield 20
    for i in range(2000000000):
         yield i

gen = generator_func()
print(next(gen)) # prints next value - now first value
print(next(gen)) # prints second value now no need to store entaire value

print(gen.__dir__())

for j in gen:
     print(type(j))
     break
