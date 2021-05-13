# import sys  
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w') 

cases = int(input())

for cas in range(cases):
	N, M = map(int, input().split())
	arr = list(map(int, input().split()))

	j = 0
	temMin = arr[0]
	temMax = arr[0]
	maxBank = []
	minBank = []
	for i in range(N):
		if arr[i] > temMax:
			temMax = arr[i]
		if arr[i] < temMax:
			temMin = arr[i]

		if j + 1 == M:
			maxBank.append(temMax)
			minBank.append(temMin)
			j = 0
			if i < N - 1:
				temMax = arr[i + 1]
				temMin = arr[i + 1] 
		else:
			j += 1

	a = min(maxBank)
	b = max(minBank)
	c = abs(a - b)
	print(c)