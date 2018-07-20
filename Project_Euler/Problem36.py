import time

def euler_36(low=1,high=1000000):
    summation = 0
    l = []
    for i in range(low,high+1):
        if bin(i)[2:] == bin(i)[:1:-1] and str(i) == str(i)[::-1]:
            summation += i
            l.append(i)            
    return summation,l

start = time.time()
print(euler_36())
print("Program took {} seconds long".format(time.time()-start))
