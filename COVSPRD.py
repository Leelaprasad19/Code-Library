# https://www.codechef.com/viewsolution/56192701
n = int(input())

for i in range(n):
    a,b = list(map(int, input().split()))
    
    #print(a,b)
    #9999999999
    if(b <= 10):
        dis = 2**b
    elif(b <= 30):
        dis = 1024 * 3**(b-10)
    else:
        dis = a
        
    if(dis > a):
        dis = a
        
    print(dis)