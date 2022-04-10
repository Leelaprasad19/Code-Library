def countDyckPaths(n):
    
    res = 1
    for i in range(0, n):
        res *= (2 * n - i)
        res /= (i + 1)
        
    return res / (n+1)
 
n = int(input())

for i in range(1,n+1):
    print("Number of Dyck Paths is :",int(countDyckPaths(i)))