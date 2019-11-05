def getDiffArray(maxArray):
	maxArray.sort()

	diffArray = []

	tem = maxArray[0]
	for i in range(len(maxArray)):
		if i+1 < len(maxArray):
			diff = abs(maxArray[i + 1] - maxArray[i])
			diffArray.append(diff)

	return diffArray

def getTopTwoMins(diffArray):

	first = second = 2147483648
	
	if len(diffArray) < 2:
		if len(diffArray) == 1:
			return diffArray[0]
	else:

		for i in range(len(diffArray)):
			if (diffArray[i] < first):
				second = first
				first = diffArray[i]
			elif (diffArray[i] > second and diffArray[i] != first):
				second = diffArray[i]
	return second



cases = int(input())

for cas in range(cases):
	#Code here
	
	N, M = map(int, input().split())

	arr = list(map(int, input().split()))

	j = 0
	array = []
	arrayOfArrays = []


	for a in arr:
		# print(j)
		if j < M:
			array.append(a)
			j += 1
			# print("if ",a)
		else:
			# print("else ",a)
			arrayOfArrays.append(array)
			array = [a]
			j = 1

	arrayOfArrays.append(array)

	maxArray = list()
	for arr in arrayOfArrays:
		maxArray.append(max(arr))

		# Get difference array
		diffArray = getDiffArray(maxArray)

		maxi, secMaxi = getTopTwoMins(diffArray)

		print(maxi, secMaxi)


		# Get max, secondMax

	