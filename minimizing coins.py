
def minimumCoins(a,n,sum_):
    
    dp = [999999999 for i in range(sum_+1)]
    dp[0] = 0
    
    for i in range(1,sum_+1):
        
        j = 0
        while(j < n and i-a[j] >= 0):
            
            dp[i] = min(dp[i],dp[i-a[j]]+1)
            
            # print(i,j,dp[i],dp[i-a[j]]+1)
            j = j + 1
            
    return dp
        
    

n = int(input())
a = list(map(int, input().split()))
sum_ = int(input())

print(minimumCoins(a,n,sum_)[-1])
