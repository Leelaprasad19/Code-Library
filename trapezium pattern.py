
def pattern(number):
    
    left = 1
    right = number * (number + 1) + 1
    
    temp = 0
    for i in range(number,-1,-1):
        
        
        if(i):
            print(" "*temp,end='')
            temp += 2
        
        for num in range(i):
            print(left,end="*")
            left += 1
            
        for num in range(i-1):
            print((right-number),end="*")
            right += 1
        
        if(i-1):   
            print(right-number)
        
        right = right - i * 2 + 2
        
        

for i in range(3,10):
    pattern(i)
    print("\n")
    
    
