for i in range(int(input())):
    n,k = list(map(int, input().split()))
    
    if(n%4==0):
        n = n
    elif(n%4==1):
        n = 1
    elif(n%4==2):
        n = n + 1
    elif(n%4==3):
        n = 0
        
        
    print(((n & (1 << (k - 1))) >> (k - 1)))
        

# temp = 0
# for i in range(1,21):
#     temp = temp ^ i
#     print(i,temp)