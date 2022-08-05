def rob(nums):
        
    n = len(nums)
        
    if(n==1):
        return nums[0]
    elif(n==2):
        return max(nums[0], nums[1])
        
    dp = [0 for i in range(n)]
        
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
        
    for i in range(2,n):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    
    sol = []
    i = n-1
    while(i >= 2):
        if(dp[i]!=dp[i-1]):
            sol.append(a[i])
            i -= 1
        i -= 1
        
    sol.append(dp[-1]-sum(sol))
    
    print(sol[::-1])       
    
    return dp[-1]
    
a = [2,7,9,3,1]
a = [6, 7, 1, 3, 8, 2, 4]
a = [5, 3, 4, 11, 2]
a = [1,2,3,1]

print(rob(a))
        
