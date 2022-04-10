# cook your dish here


for i in range(int(input())):
    
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    
    sum_ = 0
    
    count = 0
    for i in range(n):
        
        if(sum_ + a[i] <= k):
            count += 1
            sum_ += a[i]
        else:
            break
            
    if(count < n and sum_+(a[count]+1)//2 <= k ):
        count += 1
    
    print(count)
        
        
        
    
