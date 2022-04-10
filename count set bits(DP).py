def countSetBits(n):

	cnt = 0

	setBits = [0 for x in range(n + 1)]

	setBits[0] = 0

	for i in range(1, n + 1):
		setBits[i] = setBits[i // 2] + (i & 1)

	for i in range(0, n + 1):
		cnt = cnt + setBits[i]
	
	return cnt

n = 6
print(countSetBits(n))


