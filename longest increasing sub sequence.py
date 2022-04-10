def GetCeilIndex(arr, T, l, r, key):
 
    while (r - l > 1):
     
        m = l + (r - l)//2
        if (arr[T[m]] >= key):
            r = m
        else:
            l = m
 
    return r
  
def LongestIncreasingSubsequence(arr, n):
    tailIndices =[0 for i in range(n + 1)] 
    prevIndices =[-1 for i in range(n + 1)]
    len = 1
    for i in range(1, n):
     
        if (arr[i] < arr[tailIndices[0]]):
            tailIndices[0] = i
         
        elif (arr[i] > arr[tailIndices[len-1]]):
            prevIndices[i] = tailIndices[len-1]
            tailIndices[len] = i
            len += 1
         
        else:
            pos = GetCeilIndex(arr, tailIndices, -1,
                                   len-1, arr[i])
  
            prevIndices[i] = tailIndices[pos-1]
            tailIndices[pos] = i
         
    # print("LIS of given input")
    i = tailIndices[len-1]
    while(i >= 0):
        # print(arr[i], " ", end ="")
        i = prevIndices[i]
    # print()
  
    return len

arr = []
n = int(input())
for i in range(n):
    temp = int(input())
    arr.append(temp)
  
print(LongestIncreasingSubsequence(arr, n))
 