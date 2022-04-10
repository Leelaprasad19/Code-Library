def function():
    
    n = int(input())
    s = input()
    
    sol = ''
    prev = 0
    for i in range(n):
        
        if(s[i]=='1'):
            prev = prev + (i+1)
            
            if(prev%2==0):
                sol = sol + '0'
            else:
                sol = sol + '1'
        else:
            
            if(prev%2==0):
                sol = sol + '0'
            else:
                sol = sol + '1'
                
            
    print(int(sol,2)%998244353)
    

for i in range(int(input())):
    
    function()
