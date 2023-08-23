
# functions are used for code reusability
def greet(name, place):
     print(f'hello {name} welcome {place}')

greet("karthik", "home")

# write a function that take the parameters of variable length and prints it

def func(*input):
     print(input)

func([1,2,3,4]);

import re

# print(re.__doc__)

str = "Geeks for Geeks"
str.replace('for', '');

def reverse_sentence(sentence):
    words = re.findall('\S+', sentence)
    print(words)

reverse_sentence("code is goood")
