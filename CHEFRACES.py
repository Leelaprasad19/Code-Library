for i in range(int(input())):
    
    a = list(map(int, input().split()))
    
    sol = 0
    if(a[0] != a[2] and a[0] != a[3]):
        sol += 1
    
    if(a[1] != a[2] and a[1] != a[3]):
        sol += 1
    
    print(sol)