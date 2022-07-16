import math


def prime(x):
    
    if(x <= 2 or x==3):
        return True
    elif(x%2==0 or x%3==0):
        return False
    else:
        for i in range(5,int(math.sqrt(x)),6):
            if(x%i==0):
                return False
                
        return True

x = 79

if(prime(x)):
    print("Prime")
else:
    print("Composite")
