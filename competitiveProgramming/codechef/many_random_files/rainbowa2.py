

cases = int(input())
# cases = 1
for cas in range(cases):	
	N = int(input())
	arr = list(map(int, input().split()))
	jhanda = True
	Flag = False
	prev = arr[0]
	for a in arr:
		if jhanda == True:
			that = a - 1
			print("jhanda", prev, a, that)
			if (a == prev or prev == that):
				# Go forward
				Flag = True
			else:
				Flag = False
				break
			if a > 7:
				jhanda = False

		else:
			that = a + 1
			if (a == prev or prev == that):
				# Go forward
				Flag = True
			else:
				Flag = False
				

	print("yes") if Flag == True else print("no")