from functools import lru_cache
import time as t

# if I used lrucache it will memoize the computed value for the given arguement
# it will store those values in your memory
# you will be using it when you have large computations and they are relateda and repeated.

@lru_cache(maxsize=None)
def compute(num):
    t.sleep(5)
    return num*5


print(compute(2))
print(compute(4))
print(compute(2))
print(compute(4))
print(compute(4))
