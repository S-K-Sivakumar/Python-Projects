import time
def euler_29(low = 2,high = 100):
    l = []
    for i in range(low,high+1):
        for j in range(low,high+1):
            if i ** j not in l:
                l.append(i**j)
    print(len(l))
start = time.time()
euler_29()
print(("Program took {} seconds long.").format(time.time()-start))
            
