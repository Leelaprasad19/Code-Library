# cook your dish here
def function():
    s = input()
    l = len(s)
    
    count = 0
    sol = 0
    for i in range(l):
        
        if(s[i]!=s[0] and s[i]!=s[l-1]):
            count = count + 1
        else:
            count = 0
        
        sol = max(sol,count)
        
    if(sol==0):
        print(-1)
    else:
        print(sol)
        
    

t = int(input())

for i in range(t):
    function()

