# cook your dish here
def function():
    
    n = int(input())
    a = list(map(int, input().split()))
    
    pos = []
    neg = []
    
    if(a[0] < 0):
        min_ = -1*a[0]
    else:
        min_ = a[0]
    
    max_ = 0
    
    for i in range(n):
        
        if(i%2==0):
            if(a[i] < 0):
                pos.append(-1*a[i])
            else:
                pos.append(a[i])
                
            if(min_ > pos[-1]):
                min_ = pos[-1]
                
        else:
            if(a[i] < 0):
                neg.append(-1*a[i])
            else:
                neg.append(a[i])
                
            if(max_ < neg[-1]):
                max_ = neg[-1]
                
    
    if(min_ >= max_):
        print(sum(pos)-sum(neg))
    else:
        t1 = sum(pos)-min_+max_
        t2 = sum(neg)+min_-max_
        print(t1-t2)
        
    # print(pos,neg,min_,max_)
    
            

for i in range(int(input())):
    
    function()