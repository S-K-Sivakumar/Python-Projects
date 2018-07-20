import time
def euler_4(mini=100,maxi = 1000):
    max_palindrome = 0 
    for a in range(mini,maxi):
        for b in range(a+1,maxi):
            prod = a * b
            if prod > max_palindrome and str(prod) == str(prod)[::-1]:
                max_palindrome = prod
    return max_palindrome
start_time = time.time()
print(euler_4())
print(time.time()-start_time)    
