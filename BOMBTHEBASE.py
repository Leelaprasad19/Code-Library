# cook your dish here
def function():
    
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ind = 0
    for i in range(n):
        if(a[i] < x):
            ind = i+1
    print(ind)


for i in range(int(input())):
    
    function()