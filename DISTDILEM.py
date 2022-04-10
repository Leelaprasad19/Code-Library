# cook your dish here
for i in range(int(input())):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    sum_ = sum(a)
    
    i = 1
    sol = 0
    while(sum_ >= 0):
        sol += 1
        sum_ -= i
        i += 1
    
    print(sol-1)

