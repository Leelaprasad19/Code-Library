# https://www.codechef.com/viewsolution/57726321
def function(n,t):
    
    print(n*t)
    
c = int(input())

for i in range(c):
    n,t = input().split()
    
    function(int(n),int(t))