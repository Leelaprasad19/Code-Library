def function():
    
    n = int(input())
    
    # months = n/30
    temp = n//7 
    rem = n - temp * 7
    
    if(rem >= 6):
        temp += 1
    print(temp)
    # print()
    



for i in range(int(input())):
    
    function()
