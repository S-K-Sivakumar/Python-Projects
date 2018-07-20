import time
def euler_30():
    l = []
    for i in range(2,354294):
        count = 0
        for numstring in str(i):
            
            count += (int(numstring))**5
            continue
        if count == i:
            l.append(i)
    return l, str(sum(l)) + " is the sum"

start = time.time()
print(euler_30())
print(time.time() - start)

            
            
