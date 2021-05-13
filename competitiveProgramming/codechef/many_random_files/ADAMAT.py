import sys
sys.stdin = open('input.txt', 'r')

def solution1(mat, n):
	expected = 1
	for i in range(n):
		if expected == mat[0][i]:
			ansFound = True
			break
		expected += 1


	expected = 1
	continuityFlag = False

	for i in range(n):
		print(mat[i][0])

def checkIfAllTrue(arr):
	return False if False in arr else True

def solution2(mat, n):
	flagHolderOrigi = [False] * n

	for i in range(1,n+1):
		if mat[0][i-1] == i:
			flagHolderOrigi[i-1] = True

	flagHolder1 = flagHolderOrigi.copy()
	flagHolder2 = flagHolderOrigi.copy()

	# print(flagHolder)
	count1 = 0
	count2 = 0


	# print(flagHolder1, count1, "Before")
	
	while not checkIfAllTrue(flagHolder1):


		for i in range(n-1,-1,-1):
			if flagHolder1[i] is False:
				count1 += 1

				for i in range(1,i+1):
					flagHolder1[i] = False if flagHolder1[i] is True else True

	# print(flagHolder1, count1, "After")

	# print(flagHolder2, count2, "Before")

	while not checkIfAllTrue(flagHolder2):

		for i in range(n):
			if flagHolder2[i] is False:
				count2 += 1

				for i in range(1, i+1):
					if flagHolder2[i] is True:
						flagHolder2[i] =  False
					else:
						flagHolder2[i] = True


	# print(flagHolder2, count2, "After")

	return min(count1, count2)




















for testcases in range(int(input())):
	n = int(input())
	mat = list()
	ans = 0
	ansFound = False

	for i in range(n):
		arr = list(map(int, input().split()))
		mat.append(arr)

	print(solution2(mat, n))



