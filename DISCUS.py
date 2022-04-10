def function():
    
    a = list(map(int, input().split()))
    
    print(max(a[0], max(a[1],a[2])))


for i in range(int(input())):
    
    function()