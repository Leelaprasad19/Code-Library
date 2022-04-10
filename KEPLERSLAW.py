# https://www.codechef.com/viewsolution/56190230
n = int(input())

for i in range(n):
    a,b,c,d = list(map(int, input().split()))
    if(a**2/c**3==b**2/d**3):
        print("YES")
    else:
        print("NO")