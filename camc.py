cases = int(input())

for cas in range(cases):
	#Code here
	
	N, M = int(input())

	arr = list(map(int, input().split()))

	j = 0
	for a in arr:
		if j < M:
			array.append(a)
		else:
			array = []
			arrayOfArrays.append(array)
			j = 0

	print(arrayOfArrays)
	