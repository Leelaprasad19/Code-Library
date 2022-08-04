def lengthOfLIS(nums):
        
    n = len(nums)
    dp = [1]
    max_ = 1
    maxIndex = 0
        
    for i in range(1,n):
        dp.append(1)
        for j in range(i):
            if(nums[i] > nums[j] and dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1
                    
                if(dp[i] > max_):
                    max_ = dp[i]
                    maxIndex = i
    
    i = maxIndex
    sol = [nums[maxIndex]]
    while(i >= 0):
        if(dp[i]+1 == dp[maxIndex]):
            maxIndex = i
            sol.insert(0,nums[maxIndex])
        
        i-=1
        
    print(sol)
    return max_
    

arr = [0,1,0,3,2,3]
print(lengthOfLIS(arr))

