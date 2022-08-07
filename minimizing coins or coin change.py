
def minimumCoins(coins, amount):
        
    t = 2**31
    dp = [t for i in range(amount+1)]
    dp[0] = 0
        
    for i in range(len(coins)):            
        for j in range(coins[i], amount+1):
            dp[j] = min(dp[j], dp[j-coins[i]]+1)
    
    if(dp[-1]==t):
        return -1
    else:
        return dp[-1]

coins = [1,2,5]
amount = 11
print(minimumCoins(coins, amount))
