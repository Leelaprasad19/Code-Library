def longestCommonSubsequence(text1, text2):
        
    l1 = len(text1)
    l2 = len(text2)
    
    temp = [0 for i in range(l2+1)]
    dp = [list(temp) for j in range(l1+1)]
        
        
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            
            if(text1[i-1]==text2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
    return dp[-1][-1]
    
    
print(longestCommonSubsequence(input(), input()))
    
