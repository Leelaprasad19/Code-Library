def function(c,sum_,n):
    
    dp = [0 for i in range(sum_+1)]
    dp[0] = 1
    
    for i in range(1,sum_+1):
        for j in range(n):
            if(i-c[j] >= 0):
                dp[i] = dp[i] + dp[i - c[j]]
    
    print(dp)


c = [2,3,5]
n = len(c)
sum_ = 9

function(c,sum_,n)

