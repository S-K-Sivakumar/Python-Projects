import time

start_time = time.time()
def euler_1(big):
        
    ans = 0
   
    for num in range(big):
        if num % 3 == 0 or num % 5 == 0:
            ans += num
    
    return "The sum of all multiples of 3 and 5 in range %s is %s. " % (big,ans)
print(euler_1(10000))
end_time = time.time()

print("Program took %s seconds to run. " % (end_time - start_time))
