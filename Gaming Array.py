def gamingArray(a,P1,P2):
    
    x = 1
    
    val = a[0] 
    for i in a:
        if(val < i):
            val = i
            x += 1
    
    # print(x)
    if(x%2==0):
        return P2
    return P1
    

a = [7,3,1,4,6,8]
print(gamingArray(a,'BOB','ANDY'))

a = [1,3,2,4,5,7]
print(gamingArray(a,'BOB','ANDY'))

a = [6,4,2,8,5,9,7,15]
print(gamingArray(a,'BOB','ANDY'))
