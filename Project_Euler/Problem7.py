import time
def find_prime(goal):
    count = 0
    big = 200000
    
    start_time = time.time()

    for num in range(2,big+1):

           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               count += 1
               if count == goal:
                   print("The %sth prime number is %s. " % (goal,num))
                   break
    end_time = time.time()

    print("Your program took %s seconds long to run" % (end_time - start_time))


find_prime(100)




           
