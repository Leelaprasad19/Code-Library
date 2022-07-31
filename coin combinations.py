def function(sum_, c):
    
    dp = [0 for i in range(sum_+1)]
    dp[0] = 1
    
    for i in range(len(c)):
        
        for j in range(c[i], sum_+1):
            
            dp[j] = dp[j] + dp[j-c[i]]
            
    
    print(dp)

c = [1,2,3]
n = len(c)
sum_ = 4

function(sum_, c)

