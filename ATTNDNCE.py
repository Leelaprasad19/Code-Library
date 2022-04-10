d = dict()

n1,n2,n3 = list(map(int, input().split()))

def function(n):
    
    for i in range(n):
        
        x = int(input())
        
        if(x in d):
            d[x] = d[x] + 1
        else:
            d[x] = 1

function(n1)
function(n2)
function(n3)

sol = []
for key, value in d.items():
    if(value > 1):
        sol.append(key)

        
print(len(sol))
print(*sorted(sol),sep='\n')
