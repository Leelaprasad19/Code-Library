# x1 < x2 > x3 < x4 > x5 < …. xn or 
# x1 > x2 < x3 > x4 < x5 > …. xn


def AlternatingaMaxLength(nums):
		
	inc = 1
	dec = 1
		
	for i in range(1,len(nums)):
	    if(nums[i] > nums[i-1]):
	        inc = dec + 1
	    elif(nums[i] < nums[i-1]):
	        dec = inc + 1
		        
	return max(inc, dec)

arr = [10, 22, 9, 33, 49, 50, 31, 60]

print(AlternatingaMaxLength(arr))
