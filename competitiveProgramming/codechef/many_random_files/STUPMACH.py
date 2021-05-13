import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')

for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))

	# zindex = n
	# count = 0

	# while(zindex > 0):
	# 	z = zindex
	# 	for i in range(z):
	# 		if arr[i] > 0:
	# 			# print(i, z, arr)
	# 			arr[i] -= 1
	# 			count += 1
	# 		if arr[i] <= 0:
	# 			zindex = i
	# print(count)

	# mini = sys.maxsize
	# smini = sys.maxsize
	# mindex = len(arr)-1

	# mindex = arr.index(min(arr))
	# ans = max(arr[:mindex+1])

	# for i in range(len(arr)):
	# 	if arr[i] < mini:
	# 		mini = arr[i]
	# 		mindex = i

	# smini = min(arr[:mindex + 1])

	# for a in arr:
	# 	print(smini, " ", mini)
	# 	if a < mini:
	# 		smini = mini
	# 		mini = a
	# 	else:
	# 		a < smini;
	# 		smini = a

	count = 0
	mindex = len(arr)-1
	
	while mindex > 0:
		# print(mindex)
		m = min(arr)
		if m <= 0:
			mindex = arr.index(m)
			arr = arr[:mindex]

			for i in range(len(arr)):
				arr[i] -= m
				count += m
		elif m > 0:
			for i in range(len(arr)):
				arr[i] -= m
				count += m


	print(count)


