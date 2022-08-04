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
    while(i):
        if(dp[i]+1 == dp[maxIndex]):
            maxIndex = i
            sol.insert(0,nums[maxIndex])
        
        i-=1
        
    print(sol)
            
               
             
    return max_
    

arr = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(arr))

