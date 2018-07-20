import time
start_time = time.time()

l = [x**x for x in range(1,1001)]
print(str(sum(l))[-10:])
print("Program took this long: %s seconds" % (time.time() - start_time))
