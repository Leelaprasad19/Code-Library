def KadaneLongestSubArraySum(a,n):
    
    max_ = 0
    tmax = 0
    for i in a:
        
        tmax = tmax + i
        if(tmax < 0):
            tmax = 0
            
        if(max_ < tmax):
            max_ = tmax
    
    print(max_)
    

a = [1,2,3,-5,-8,5,7,-2,9]
n = len(a)

KadaneLongestSubArraySum(a,n)


