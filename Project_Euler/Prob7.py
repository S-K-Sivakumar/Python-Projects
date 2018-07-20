def prime():
    for num in range(2,101):
        if all(num%i!=0 for i in range(2,num)):
            yield(num)
    
print(prime())
