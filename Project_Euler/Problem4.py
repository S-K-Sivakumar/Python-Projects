def euler_4():
    
    for num in range(1,232792561):
                       
        count = 0
        for i in range(1,21):
            
            if num % i != 0:
                continue
            if num % i == 0:
                count += 1
                
            
            if count == 20:
                return num
                
        
            
print(euler_4())
