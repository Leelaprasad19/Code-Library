s1 = input()
s2 = input()

n1 = len(s1)
n2 = len(s2)

temp = [0 for i in range(n1+1)]
dp = [list(temp) for i in range(n2+1)]

for i in range(1, n2+1):
    for j in range(1,n1+1):
        if(s2[i-1]==s1[j-1]):
            dp[i][j] = dp[i-1][j] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
print(*dp,sep='\n')
