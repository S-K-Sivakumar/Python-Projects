#It can be seen that the number, 125874, and its double, 251748,
#contain exactly the same digits, but in a different order. Find
#the smallest positive integer,x, such that 2x, 3x, 4x, 5x, and 6x,
#contain the same digits.

import time
start_time = time.time()
def euler_52(to = 1000000):
    for i in range(1,to):
        x1 = sorted(str(i))
        x2 = sorted(str(i*2))
        x3 = sorted(str(i*3))
        x4 = sorted(str(i*4))
        x5 = sorted(str(i*5))
        x6 = sorted(str(i*6))
        
        if x1 == x2 == x3 == x4 == x5 == x6:
            break
        else:
            continue
    return(i)

print(euler_52())
end_time = time.time()
print("Your program took %s seconds long." % (end_time - start_time))
