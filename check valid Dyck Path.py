def checkDyckPath(s):
    x = 0
    y = 0
    for i in s:
        if(i=='x'):
            x+=1
        else:
            y+=1
        
        if(x < y):
            return 0
    
    if(x!=y):
        return 0
        
    return 1
 
s = input()

if(checkDyckPath(s) and len(s)%2==0):
    print("Valid Path")
else:
    print("Invalid Path")
