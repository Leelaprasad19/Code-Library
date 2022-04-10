#https://www.codechef.com/viewsolution/57735916

def function(s,k,l):
    
    n = l//2
    c = 0
    for i in range(n):
        if(s[i]!=s[l-i-1]):
            c+=1

    m = k - c
    if(m >= 0 and m%2==0):
        print("YES")
    elif(m >= 0 and l%2==1):
        print("YES")
    else:
        print("NO")

cases = int(input())

for i in range(cases):
    
    l,k = input().split()
    s = input()
    
    l = int(l)
    k = int(k)
    
    
    function(s,k,l)
    