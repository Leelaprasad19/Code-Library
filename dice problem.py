
import time

def diceValue_(n):
    
    dp = [0 for i in range(n+1)]
    
    dp[0:7] = [1,1,2,4,8,16,32]
    
    for i in range(7,n+1):
        
        dp[i] = dp[i-1]*2 - dp[i-7]
        # print(dp[i-1],dp[i-7])
    
    return dp
    
    

def diceValue(n):
    
    dp = [0 for i in range(n+1)]
    
    dp[0] = 1
    
    for i in range(1,n+1):
        
        j = 1
        
        while(i-j >= 0 and j <= 6):
            
            dp[i] = dp[i] + dp[i-j]
            j = j + 1;
            
    return dp
    
n = int(input())

t0 = time.time()
print(diceValue(n)[n])
# diceValue(n)[n]
t1 = time.time()
print(diceValue_(n)[n])
# diceValue_(n)[n]
t2 = time.time()


print("{:.8f} {:.8f}".format(t1-t0,t2-t1))

if(t1-t0 > t2-t1):
    print('Efficient')

