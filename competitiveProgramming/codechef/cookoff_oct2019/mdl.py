def findMed(arr):

	a = arr[0:3]
	a.sort()
	mid = a[1]

	arr.remove(mid)

	# for i in range(0,3):
	# 	if arr[i] == mid:
	# 		arr[i]



cases = int(input())

for cas in range(cases):

	df = input()

	arr = list(map(int, input().split()))

	while(len(arr) > 2):
		findMed(arr)

	for ar in arr:
		print(ar, end=" ")

	print()