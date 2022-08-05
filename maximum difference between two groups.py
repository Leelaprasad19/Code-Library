def CalculateMax(arr, n):
 
    arr.sort()
    min_sum = sum(arr[:n//2])
    max_sum = sum(arr[n//2:])
    return abs(max_sum - min_sum)
 
arr = [6, 7, 2, 5 ,1, 11]
n = len(arr)
print(CalculateMax(arr, n))
