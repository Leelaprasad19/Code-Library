

for i in range(int(input())):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    even = 0
    odd = 0
    for i in a:
        if(i%2==0):
            even += 1
        else:
            odd += 1
    
    if(odd % 2 == 0):
        temp = odd // 2
        if(temp < even):
            print(temp)
        else:
            print(even)
    else:
        print(even)
    
        
        
