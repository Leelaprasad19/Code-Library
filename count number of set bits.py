d = dict()

n = int(input())
lst = list(map(int, input().split()))

count = 0
for temp in lst:
    
    if(temp in d):
        count = count + d[temp]
    else:
        val = bin(temp)[2:]
        x = val.count('1')
        d[temp] = x
        count = count + x
    # print(count)
print(count)