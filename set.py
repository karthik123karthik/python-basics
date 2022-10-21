# creating a set- unordered, mutable , no duplicates
myset1 = set()
myset = {1, 2, 3, 4, 4}
myset = set("Hello")
print(myset)

# operations on set
myset1.add(1)
myset1.add(2)
myset1.add(3)
print(myset1)
myset1.remove(3)
print(myset1)
myset1.discard(4)  # not give error
myset1.pop()  # returns an arbitrary value and removes it

# itearating the set
for i in myset1:
    print(i)

# if with set
if 2 in myset1:
    print("YES")
else:
    print("NO")

# set operations
odds = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}
prime = {2, 3, 5, 7}

u = odds.union(even)
print(u)
i = odds.intersection(prime)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diffA = setA.difference(setB)
print(diffA)
diffB = setA.symmetric_difference(setB)
print(diffB)  # prints the elemenst other than itersection parts

# setA.update(setB)  # alters the original set
# setA.intersection_update(setB)  #prints the intersection part
# setA.difference_update(setB)  #prints the difference part
# print(setA)

print(setA.issubset(setB))  # is A subset of B

# copying
setC = setA  # this is by reference
setC = setA.copy()  # this is by value

# frozenset cannot be changed after creation immutable set
a = frozenset("Hello")
# a = set("BYE")
print(a)








