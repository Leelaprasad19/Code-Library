# cook your dish here

n,m = list(map(int, input().split()))
compounds = list(map(int, input().split()))

for i in range(m):
    
    curBreaking, numberOfBreaking = list(map(int, input().split()))
    
    breakingCompounds = list(map(int, input().split()))
    
    update = []
    
    for i in range(0,2*numberOfBreaking,2):
        
        temp = compounds[curBreaking-1] * breakingCompounds[i]
        # compounds[breakingCompounds[i+1]-1] += temp
        update.append([breakingCompounds[i+1]-1,compounds[breakingCompounds[i+1]-1] + temp])
    
    compounds[curBreaking-1] = 0
    
    for i in update:
        compounds[i[0]] = i[1]
    
    # for i 
    # print(update)
    

        
# print(*compounds,sep=' ')
mod = 10**9+7
for i in compounds:
    print(i%mod,end=' ')

