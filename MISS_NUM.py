def function(s,val1,val2,o1,o2):
    
    sum_  = val1
    diff = val2
    if(val2 > sum_):
        sum_ = val2
        diff = val1
    
    sol1 = int(s)
    sol2 = sum_ - sol1
    
    
    if(sol1 <= 0 or sol2 <= 0):
        return False
    
    if(sol1 > 10000 or sol2 > 10000):
        return False
    
    if(sol1*sol2==o1 and sol1//sol2==o2):
        print(sol1,sol2)
        return True
    elif(sol1*sol2==o2 and sol1//sol2==o1):
        print(sol1,sol2)
        return True
    else:
        return False


for i in range(int(input())):
    
    n1,n2,n3,n4 = list(map(int, input().split()))
    
    c = 0
    if(n1==0):
        c += 1
    if(n2==0):
        c += 1
    if(n3==0):
        c += 1
    if(n4==0):
        c += 1
    
    if(c > 1):
        print(-1,-1)
        continue
    
    s1 = (n1 + n2)/2
    s2 = (n3 + n4)/2
    if(s1 - int(s1)==0):
        if(function(s1,n1,n2,n3,n4)):
            continue
    
    if(s2 - int(s2)==0):
        if(function(s2,n3,n4,n1,n2)):
            continue
        # if(function(s2,n1,n2)):
        #     continue
    
    s1 = (n1 + n3)/2
    s2 = (n2 + n4)/2
    if(s1 - int(s1)==0):
        if(function(s1,n1,n3,n2,n4)):
            continue
        # if(function(s1,n2,n4)):
        #     continue
    
    if(s2 - int(s2)==0):
        if(function(s2,n2,n4,n1,n3)):
            continue
        # if(function(s2,n1,n3)):
        #     continue
        
        
    s1 = (n1 + n4)/2
    s2 = (n2 + n3)/2
    if(s1 - int(s1)==0):
        if(function(s1,n1,n4,n2,n3)):
            continue
        # if(function(s1,n2,n3)):
        #     continue
    
    if(s2 - int(s2)==0):
        if(function(s2,n2,n3,n1,n4)):
            continue
        # if(function(s2,n1,n4)):
        #     continue
    
    print(-1,-1)
        

