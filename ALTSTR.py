def function():
    
    n = int(input())
    s = input()
    
    cones = 0
    czeros = 0
    
    for i in s:
        
        if(i == '1'):
            cones += 1
        else:
            czeros += 1
    
    if(cones==czeros):
        print(cones+czeros)
    elif(cones > czeros):
        print(czeros*2+1)
    else:
        print(cones*2+1)
        
    
    


for i in range(int(input())):
    
    function()
