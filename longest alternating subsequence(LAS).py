def LAS(arr, n):

	inc = 1
	dec = 1
	
	for i in range(1,n):
	
		if(arr[i] > arr[i-1]):
		    inc = dec + 1
		elif(arr[i] < arr[i-1]):
			dec = inc + 1
			
	return max(inc, dec)


arr = [10, 22, 9, 33, 49, 50, 31, 60]
n = len(arr)

print(LAS(arr, n))

