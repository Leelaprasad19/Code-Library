def getCompositeNumbers(n):
    
    sol = []
    prime = [True for i in range(n+1)]
     
    p = 2
    while(p * p <= n):
        
        if (prime[p] == True):
              
            for i in range(p * p, n + 1, p):
                prime[i] = False
                
        p += 1
        
    c = 0
 
    for p in range(2, n):
        if not prime[p]:
            sol.append(p);
            c += 1
            
    return c,sol
 
n = int(input('Enter range - '))

c,a = getCompositeNumbers(n)

print("Total Composite numbers in range :", c)
print("The Composite numbers are - ")
print(a)