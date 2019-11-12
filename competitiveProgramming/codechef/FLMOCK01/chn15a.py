
test = int(input())

for t in range(test):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))

	count = 0 

	for a in arr:
		a += k
		if a % 7 == 0:
			count += 1
	print(count)