# import sys  
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output2.txt', 'w')
 
def checkDivi(sss, m):
	te = ''.join(sss)
	te = int(te,2)
	if te % m == 0:
		return True
	else:
		return False
def generateBin(n, pre, generatedBinList):
	# Base case
	if (n == 0):
		# print(pre)
		generatedBinList.append(pre)
	# Else
	else:
		#	print 0s recursively
		generateBin(n - 1, pre + '0', generatedBinList)
		#	print 1s recursively
		generateBin(n - 1, pre + '1', generatedBinList)

test = int(input())

for t in range(test):
	n, m = map(int, input().split())
	ss = input()
	_pos = []
	sss = [] #Each char listified for mutability

	for i in range(len(ss)):
		if ss[i] == '_':
			_pos.append(i)
			sss.append(ss[i])
		else:
			sss.append(ss[i])

	# print(_pos)
	generatedBinList = []
	count = 0 #For coumting divisible numbers

	generateBin(len(_pos), '', generatedBinList)
	# print(generatedBinList)

	
	for gen in generatedBinList:
		i = 0
		for p in _pos:
			sss[p] = gen[i]
			i += 1
		if checkDivi(sss, m):
			count += 1

	print(count)

	


