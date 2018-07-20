import time,numpy
start_time = time.time()
def euler_4_practice():
    for num in range(110,9802):
        stringnum = str(num)
        if stringnum == stringnum[::-1]:
            factor = int(num ** 0.5)
            if isinstance(factor,int):
                return factor
            else:
               continue
        else:
            continue
    
    
        
        

print(euler_4_practice())
    
