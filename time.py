import time

# time.time() gives seconds from the epoch time
# time.sleep(3) programs waits for 3 secvonds before executing next line
t = time.localtime()
print(time.strftime("%D",t))
