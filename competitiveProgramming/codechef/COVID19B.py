import sys
sys.stdin = open('input.txt', 'r')

def solution1(n, arr):
	"""
	Looking at the next decresing number in the right
	"""
	globalMax = -1
	globalMin = 99999999999999

	cascadeCount = 0

	for i in range(n):
		if i+1 < n:
			if arr[i] == arr[i+1] + 1:
				cascadeCount += 1

	# print("cascade", cascadeCount)


	for i in range(n):
		collect = 0

		for j in range(i,n):
			if j+1 < n:
				# print("arr", arr[j], arr[j+1])
				if arr[j] > arr[j+1]:
					collect += 1
		# print(collect)
		globalMax = collect if globalMax < collect else globalMax

		if cascadeCount+1 == n:
			globalMin = cascadeCount
		else:
			globalMin = collect if globalMin > collect else globalMin
	print(globalMin+1, globalMax+1)

def getTime(i, j, Vi, Vj):
	if Vi - Vj <= 0:
		return -1
	else:
		return (j-i)/(Vi-Vj)

def getMinMax(timeOfMeet):
	positive = 0
	for time in timeOfMeet:
		if time > 0:
			positive += 1

def getMinimumNumber(n, arr):
	minimumAnswer = 99999999999
	for i in range(n):
		if arr[i] < 0:
			if i-1 >= 0:
				sameNumber = arr[i-1]
				sameNumberFoundCount = 0
				for j in range(i-1,-1,-1):
					if j >= 0:
						if arr[j] == sameNumber:
							# print("sameNumber found", arr[j])
							if sameNumberFoundCount is None:
								sameNumberFoundCount = 1
							else:
								sameNumberFoundCount += 1
						else:
							break
				if sameNumberFoundCount is not None:
					minimumAnswer = sameNumberFoundCount if minimumAnswer > sameNumberFoundCount else minimumAnswer
	minimumAnswer = minimumAnswer+1 if minimumAnswer > 1 else minimumAnswer
	# print("minimumAnswer = ",minimumAnswer)
	return minimumAnswer

def getMinimumNumber2(n, arr, velocities):
	# print(arr) 
	if velocities[0] == 0:
		return 1
	if arr[0] < 0:
		return 1
	throwAwayList = list()
	masterThrowAwayList = list()

	for i in range(n):
		if arr[i] < 0:
			throwAwayList = []
			yesFirst = True
			prev = 9999999999999
			for j in range(i-1,-1,-1):
				if arr[j] > 0:
					if yesFirst:
						throwAwayList.append(arr[j])
						prev = arr[j]
						yesFirst = False
					elif arr[j] == prev:
						throwAwayList.append(arr[j])
				else:
					masterThrowAwayList.append(len(throwAwayList))
					throwAwayList = list()
					prev = 999999999999999
					continue

			masterThrowAwayList.append(len(throwAwayList))

	# print("masterThrowAwayList = ", masterThrowAwayList)
	return min(masterThrowAwayList) + 1


def getMaximumNumber(n, arr):
	# Finding same in continuation
	# Finding increasing continuation
	# print(arr)
	maxAnswer = 0
	prev = arr[0]
	tempMax = -1

	for i in range(n):
		if arr[i] <= 0:
			tempMax = -1
			continue
		if arr[i] >= prev:
			tempMax = tempMax+1 if tempMax > 0 else 2
		else:
			maxAnswer = tempMax if tempMax > maxAnswer else maxAnswer
			tempMax = 2
		maxAnswer = tempMax if tempMax > maxAnswer else maxAnswer
		prev = arr[i]

	maxAnswer = 1 if maxAnswer == 0 else maxAnswer
	# print("maxAnswer = ", maxAnswer)
	return maxAnswer

def getMaximumNumber2(n, arr):
	# print(arr)
	prev = arr[0]
	throwAwayList = list()
	masterThrowAwayList = list()
	for a in arr:
		if a >= prev and a > 0:
			# print(a, end=" ")
			throwAwayList.append(a)
		else:
			masterThrowAwayList.append(len(throwAwayList))
			throwAwayList = list()
		prev = a

	# print("masterThrowAwayList = ", masterThrowAwayList)
	# print("max is = ", max(masterThrowAwayList) + 1)
	return max(masterThrowAwayList) + 1

def solution2(n, arr):
	timeOfMeet = [-1]*n

	for i in range(n):
		if i+1 < n:
			t = getTime(i, i+1, arr[i], arr[i+1])
			timeOfMeet[i] = t

	# print(timeOfMeet)
	# p = getMinimumNumber(len(timeOfMeet), timeOfMeet)
	p = getMinimumNumber2(len(timeOfMeet), timeOfMeet, arr)

	q = getMaximumNumber2(len(timeOfMeet), timeOfMeet)
	# print()
	print(p, q)



























for test in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	
	solution2(n, arr)