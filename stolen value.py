def function(a,n):
    
    dp = [0 for i in range(n)]
    dp[1] = a[0]
    
    for i in range(2,n):
        dp[i] = max(dp[i-2]+a[i], dp[i-1])
    
    print(dp)

arr = [9, 3, 5, 8, 2, 4, 7]
n = len(arr)

function(arr,n)
