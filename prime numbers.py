import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True
 
c = 0
sol = []
n = int(input('Enter range - '))
 
for i in range(n):
    if(is_prime(i)):
        c += 1
        sol.append(i)
    
print("Total prime numbers in range :", c)
print("The prime numbers are - \n",sol)
