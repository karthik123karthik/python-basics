# map ,filter and reduce are the higher order functions(the functions which take functions as an arguement)
# we need to pass iterables.

l = [1,2,3,4,5,6,7,8]
newl = list(map(lamda x:x*2,l)) #this will return a map object
newl = list(filter(lamda x:x>2,l)) #this will return a filter object.
sum = reduce(lamda x,y:x+y, l) #this returns the sum of the list
