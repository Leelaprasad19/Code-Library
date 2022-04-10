def function():
    n = int(input())
    s = input()
    
    ones = 0
    zeros = 0
    
    for i in range(n):
        
        if(s[i]=='1'):
            ones += 1
        else:
            zeros += 1
    
    flag1 = True
    flag2 = True
    for i in range(0,n-1,2):
        
        if(s[i]!='0' or s[i+1]!='1'):
            flag1 = False
        
        if(s[i]!='1' or s[i+1]!='0'):
            flag2 = False
    
    if(flag1 or (flag2 and s[n-1]=='1')):
        print(n//2)
        return 0
    
    if(ones == zeros):
        print(ones-1)
    else:
        print(min(ones,zeros))


for i in range(int(input())):
    
    function()