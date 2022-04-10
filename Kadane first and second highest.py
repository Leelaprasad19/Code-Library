import sys
def kadane(A):
 
    if len(A) <= 1:
        return 0,len(A)-1,sum(A)
 
    maxSoFar = -sys.maxsize
 
    maxEndingHere = 0
 
    start = 0
    end = 0

    beg = 0

    for i in range(len(A)):

        maxEndingHere = maxEndingHere + A[i]

        if maxEndingHere < A[i]:
            maxEndingHere = A[i]
            beg = i
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
            start = beg
            end = i
    return start,end,maxSoFar

n = int(input())
my_array = list(map(int,input().split()))
for i in range(2):
    if len(my_array)>0:
        start,end,maxs = kadane(my_array)
        j = end
        while(j>=start and j<=end):
            my_array.pop(j)
            j-=1

        print(maxs)
    else:
        print(0)