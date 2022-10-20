# same as list but it is immutable

# creating a tuple
mytuple = ()  # paranthesis are optional
print(mytuple)

mytuple2 = tuple(["karthik", 28, 0, 1, 2, 1, 0])
print(mytuple2)

# accesing items of tuple
item = mytuple2[-2]
print(item)

# if else checking
if "karthik" in mytuple2:
    print("yes")
else:
    print("no")

# getting length of a tuple
print(len(mytuple2))

# getting the count of an item
print(mytuple2.count(29))
print(mytuple2.index(1))  # returns the first index of the array
mylist = list(mytuple2)
print(mylist.index(1))

# slicing i tuple
mytuple3 = mytuple2[::-1]
print(mytuple3)

# unpacking a tuple
mytuple4 = "Karthik", 28, "B-tech"
name, *age, degree = mytuple4
print(age)

name, age, *other = mylist
print(other)

# tuples are more efficient than lists

