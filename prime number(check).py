import math

def checkPrime(number):
    
    if(number <= 3):
        return True
    
    if(number%2==0):
        return False
    
    for i in range(3, int(math.sqrt(number))+1,2):
        
       if(number%i==0):
           return False
        
    return True

x = 79

if(checkPrime(x)):
    print("Prime")
else:
    print("Composite")
