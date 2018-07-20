import time
def euler_6(n):
    sum_squares = 0
    for i in range(1,n+1):
        sum_squares += i**2
    l = [i for i in range(1,n+1)]
    square_sum = sum(l) ** 2
    return square_sum - sum_squares
start_time = time.time()
print(euler_6(100))
Time = (time.time() - start_time)
print(Time)
        
