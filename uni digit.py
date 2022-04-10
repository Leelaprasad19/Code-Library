def cycles(x):
    
    m = x%10
    x = x%10
    
    sol = []
    i = 0
    while(i < 4):
        if(x not in sol):
            sol.append(x)
        else:
            break
        x = m * x
        x = x%10
        i+=1
        
    return sol
        

def function(x,y):
    
    cycle = cycles(x)
    den = len(cycle)
    
    ind = y%den
    print(cycle[ind-1])
    


x = int(input())
y = int(input())

# for i in range(10):
#     cycles(i)

for i in range(4):
    function(x,y+i)
    print(x**(y+i)%10)

