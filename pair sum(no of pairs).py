def getPairsCount(arr, n, sum):

	m = [0] * 1000

	for i in range(0, n):
		m[arr[i]] += 1

	twice_count = 0

	for i in range(0, n):

		twice_count += m[sum - arr[i]]
		
		if (sum - arr[i] == arr[i]):
			twice_count -= 1

	return int(twice_count / 2)


arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6

print("Count of pairs is", getPairsCount(arr, n, sum))

