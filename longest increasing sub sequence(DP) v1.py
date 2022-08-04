def lengthOfLIS(nums):
        
    n = len(nums)
    dp = [1]
    max_ = 1
        
    for i in range(1,n):
        dp.append(1)
        for j in range(i):
            if(nums[i] > nums[j] and dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1
                    
                if(dp[i] > max_):
                    max_ = dp[i]
             
    return max_
    

arr = [10,9,2,5,3,7,101,18]
arr = list(map(int, input().split()))
print(lengthOfLIS(arr))
