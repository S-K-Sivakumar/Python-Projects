import time
def euler_16(n):
    summation = 0
    for num in str(2**n):
        summation += int(num)
    return summation
start = time.time()
print(euler_16(100000))
print(time.time() - start)
