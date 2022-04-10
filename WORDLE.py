def function():
    
    sol = ''
    s = input()
    t = input()
    
    for i in range(len(s)):
        
        if(s[i]==t[i]):
            sol += 'G'
        else:
            sol += 'B'
            
    print(sol)


for i in range(int(input())):
    
    function()