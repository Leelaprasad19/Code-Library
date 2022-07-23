import math

def nthPrime(n):
    
    num = 2
    prime = 0
    
    while(n):
        
        flag = True
        
        if(num==2):
            flag = True
        elif(num%2==0):
            flag = False
        else:
            for i in range(3,math.floor(math.sqrt(num))+1,2):
                
                if(num%i==0):
                    flag = False
                    break
             
        if(flag):
            prime = num
            n = n - 1
        
        num = num + 1
    
    print(prime)


for i in range(1,169):
    nthPrime(i)                
    
