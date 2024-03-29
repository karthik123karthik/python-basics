# creating a list
mylist = []
print(mylist)  # prints an empty list can also be used to copy a list into other

mylist2 = list(["karthik", "g k", "kar86600@gmail.com", "frontend development"])
print(mylist2)  # prints an empty list

# elements inside a list.
# list can have different data-types inside it because python is dynamically typed
mylist = ["karthik", 20, "engineering", "Male"]
print(mylist)

# getting a list item
item = mylist[0]
print(item)

# iterating a list
for item in mylist:
    print(item)

# using in operator
if "karthik" in mylist:
    print("yes")
else:
    print("no")

# length of a list
print(len(mylist))

# appending items to the list
mylist.append("UVCE")
print(mylist)

#extract method
mylist.extend([1,2,3])
print(mylist) # added the each element at the end of the list

mylist.insert(1, "CSE")
print(mylist)

# removing items from the list
last = mylist.pop() # it takes the index
# pop will return the item it have removed
print(mylist)

mylist.remove("CSE") # it removes the first occurence and takes value
# it will not return anything
print(mylist)

mylist.clear()
print(mylist)

# sorting and reversing a list
mylist2.reverse()
print(mylist2)

mylist2.sort()  # alters the original array
print(mylist2)

new_list = sorted(mylist2)  # returns  the new sorted array
print(new_list)

new_list = new_list + mylist2  # concating 2 strings
print(new_list)

# some tricks while creating a list
mylist3 = [0]*5  # returns a list with 5 zeros [0, 0, 0, 0, 0]
print(mylist3)

# slicing of a list
mylist4 = new_list[1:4:2]  # starting index will be included but the ending will be excluded
print(mylist4)

mylist4 = new_list[::-1] #reverse a list
print(mylist4)

# copy a string
# list4_cpy = mylist4
list4_cpy = mylist4.copy()
list4_cpy.remove("karthik")
print(list4_cpy)
print(mylist4)

# list comprehension
mylist4 = [item + item for item in mylist4]
print(mylist4)

# iterating over two lists parallel
ls1 = [1,2,3,4,5]
ls2 = [5,6,7,8,9]

for item in list(zip(ls1, ls2)):
    print(*item) # prints ( 1 5 , 2 6, 3 7, 4 8, 5 9)

for idx, item in enumerate(ls1):
    print(idx, item) # prints index then item




