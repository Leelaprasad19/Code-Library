# cook your dish here
def function():
    
    n = int(input())
    a = input()
    
    time = 0
    
    i = 0
    while(i < n):
        
        if(i+1 < n):
            if(a[i] != a[i+1]):
                time += 1
                i += 1
            elif(a[i]==a[i+1]):
                time += 1
                i += 2
        else:
            time += 1
            i += 1
    
    print(time)


for i in range(int(input())):
    
    function()
