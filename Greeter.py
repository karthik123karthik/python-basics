import time

# print(time.gmtime(0))
# curr = time.time() # returns current time
# print(time.ctime(curr))
hour  = int(time.strftime("%H"))
print(hour)

if (hour<12):
    print("Good Morning Sir have a great day")
elif (hour>=12 and hour <=17):
    print("Good Morning Sir")
elif (hour>=17 and hour<=19):
    print("Good Evening Sir")
else:
    print("Good night Sir")
