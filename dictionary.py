# dictionaries are mutable and unordered stores key value pairs
mydict = {"name": "karthik", "age": 28, "study": "B-Tech"}
print(mydict)

mydict = dict(name="karthik", age=28, study="B-tech")
print(mydict)

mydict2 = dict(mydict)

# accesing dictionary elements
print(mydict["name"])

# adding new key value pair
mydict["sex"] = "male"
print(mydict)

# removing elements from dict
del mydict["sex"]
print(mydict)

mydict.pop("name")
print(mydict)

mydict.popitem()  # removes last element
print(mydict)

# iterating the dictionary

for key in mydict2.keys():
    print(key)

for value in mydict2.values():
    print(value)

for key, value in mydict2.items():
    print(key, value)

# merging two tuples
mydict3 = {"sex": "M"}
mydict3.update(mydict2)
print(mydict3)

# we cannot use list as key but can use tuples

