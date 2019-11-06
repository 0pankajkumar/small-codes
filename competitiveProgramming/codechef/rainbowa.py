def check(aa, arr, currentIndex, registerDict):
	for a in arr:
		if a != aa[currentIndex]:
			currentIndex += 1
			if a != aa[currentIndex]:
				return False
		else:
			if a not in registerDict:
				registerDict[a] = 1
			else:
				if currentIndex <= 6:
					registerDict[a] += 1
				else:
					registerDict[a] -= 1

	for keys, values in registerDict.items():
		if registerDict[keys] != 0:
			return False

	return True


cases = int(input())
# cases = 1
for cas in range(cases):	
	N = int(input())
	arr = list(map(int, input().split()))
	# W = [6, 7, 9, 13]

	aa = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
	currentIndex = 0
	registerDict = dict()

	if check(aa, arr, currentIndex, registerDict):
		print("yes")
	else:
		print("no")

	


