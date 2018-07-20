import time
start_time = time.time()
def euler_2():
    
    count = 0
    fib = [0]
    evenfib = []
    a = 0
    b = 1
    while max(fib) <= 3000000:   
            c = a + b
            fib.append(b)
            
            a = b
            b = c
            count += 1
    for num in fib:
        if num % 2 ==0:
            evenfib.append(num)
    return (sum(evenfib))
print(euler_2())
end_time = time.time()
t = end_time - start_time
print("This program took %s seconds to run. " % t)
    




    
