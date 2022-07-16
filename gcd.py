
def gcd(x,y):
    
    if(y==0):
        print(x)
    else:
        gcd(y, x%y)

x = 6
y = 15

gcd(x,y)

