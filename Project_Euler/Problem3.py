def largest_prime(big):
    factors = []
    primes = []
    yes = []

    factors = [small for small in range(3,big+1) if big % small == 0]
    
   
    for num in range(2,big+1):
    
       for i in range(2,num):
           if (num % i) == 0:
               break
           else:
               primes.append(num)
    for factor in factors:
        if factor in primes:
            break
        return factor
        

print(largest_prime(350))
    
