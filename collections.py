from collections import Counter, deque, namedtuple;

# create a counter object
ans = '123456665233445234623466464'
counterobj = Counter(ans)
print(counterobj)

# creating a stack using deque
stack = deque([])
stack.append(1) # append to the left
print(stack.pop()) #delete to the left
stack.appendleft(1)
print(stack.popleft())
