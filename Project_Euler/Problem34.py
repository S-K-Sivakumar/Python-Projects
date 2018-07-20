def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def euler_34():
    addition = 0
    l = []
    for i in range(3,100000):
        summation = 0
        for stringnum in str(i):
            summation += factorial(int(stringnum))
        if summation == i:
            addition += i
            l.append(i)
    return addition, l

print(euler_34())
        
