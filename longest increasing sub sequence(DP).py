n = int(input())

lis = []
a = []
max_ = 1
for i in range(n):
    
    temp = int(input())
    a.append(temp)
    lis.append(1)
    
    for j in range(i):
        if(a[i] > a[j] and lis[i] < lis[j]+1):
            lis[i] = lis[j] + 1
            if(lis[i] > max_):
                max_ = lis[i]
    
print(max_)