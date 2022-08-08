def getPrimeNumbers(n):
    
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
        if prime[p]:
            sol.append(p);
            c += 1
            
    return c,sol
 
n = int(input('Enter range - '))

c,a = getPrimeNumbers(n)

print("Total prime numbers in range :", c)
print("The prime numbers are - ")
print(a)
