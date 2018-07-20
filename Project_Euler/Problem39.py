from math import ceil
import time
def euler_39(sub,p):
    
    d = {}
    
    for i in range(p-sub,p+1):
        
        count = 0
        for a in range(1,ceil(p/2)):
            for b in range(a,ceil(p/2)):
                c = (a**2 + b**2) ** 0.5
                if a + b + c == i:
                    
                    count += 1

        if count > 3:
            d[str(i)] = count
        
        
    return d
start = time.time()
print(euler_39(10,840))
print("Program took {} seconds long.".format(time.time() - start))
                    
