import time
def factorial(n,product=1):
    for i in range(n,1,-1):
        product *= i
    return product
start_time = time.time()
s = str(factorial(2000))
sum = 0
for num in s:
    sum += int(num)

print(sum)
end_time = time.time()
Time = end_time - start_time
print(Time)
    
