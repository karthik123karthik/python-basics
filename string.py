# strings: ordered, immutable, text representation

my_string = '''I'm karthik g k the best person in the world'''
print(my_string)

print(my_string.capitalize()) #capitalizes the given string.
# accessing a string
char = my_string[0]
print(char)

# accesing substring by slicing
substring = my_string[2:5]
print(substring)

# concatination of string
greeting = "Hello"
name = "karthik"
greet = greeting + name
for i in greet:
    print(i, end=" ")


# inside if statement
if 'k' in greet:
    print("\nYES")
else:
    print("NO")

# strip method on string
name = "  karthik  "
print(name.strip())# removes any leading spaces or ending spaces
print(name.strip("abc")) #among abc if any is present in the beginning and the ending of the string it will be removed.
print(name.swapcase()) #converts upper case into lower and lower into uppercase
print(name.upper())
print(name.lower())
print(name.startswith(' '))
print(name.endswith('   '))
print(my_string.find('lo'))  # returns the index if not returns -1
print(my_string.index('lo')) # gives an error if the string given is not present
print(my_string.count('o'))
print(my_string.replace('karthik', 'universe'))

# list and strings
my_string = "how are you doing"
my_list = my_string.split(' ')
print(my_list)
my_string = ' '.join(my_list)
print(my_string)
new_list = ['6']*6
my_string = ''.join(new_list)
print(my_string)

#  one more topic is f strings
var = "karthik"
new_string = f"my name is {var}"
print(new_string)
