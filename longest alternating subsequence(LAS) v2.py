# x1 < x2 > x3 < x4 > x5 < …. xn or 
# x1 > x2 < x3 > x4 < x5 > …. xn


def AlternatingaMaxLength(nums):
		
	inc = 1
	dec = 1
	
	sol = [nums[0]]
		
	flag = 0	
	
	for i in range(1,len(nums)):
	    if(nums[i] > nums[i-1]):
	        inc = dec + 1
	        if(flag!=1):
	            sol.append(nums[i])
	            flag = 1
	        else:
	            sol.pop()
	            sol.append(nums[i])
	    elif(nums[i] < nums[i-1]):
	        dec = inc + 1
	        if(flag!=2):
	            sol.append(nums[i])
	            flag = 2
	        else:
	            sol.pop()
	            sol.append(nums[i])
		        
	print(sol)
	return max(inc, dec)

arr = [10, 22, 9, 33, 49, 50, 31, 60, 5, 7, 98, 45, 342, 324, 12, 345, 45, 32, 908,3,23,435]

print(AlternatingaMaxLength(arr))



