# https://www.codechef.com/viewsolution/57691768
n,d = input().split()
n = int(n)
d = int(d)

a = []
for i in range(n):
    temp = int(input())
    a.append(temp)

a.sort()

# print(a)
c = 0

i = 0
while(i < n-1):
    
    # print(a[i+1],a[i],a[i+1]-a[i])
    if(a[i+1]-a[i] <= d):
        c+=1
        i+=1
    i+=1

print(c)
