# Calculating each square individually & memoizing to optimize
import math
squareBank = dict()

def decideRange(N):
	t = ['', '']
	for i in range(N):
		t[0] += '1'
		t[1] += '9'
	return (int(t[0]), int(t[1]))


def itDosentHasZeros(p):
	s = str(p)
	ct = s.count('0')
	return True if ct == 0 else False

def isPerfectSquare(x): 
	# print("Checking perfect square for ", x)
	sr = math.sqrt(x) 
	# return ((sr - math.floor(sr)) == 0) 
	return True if sr in squareBank else False

def getSumOfSquare(aa):
	# print("aa is ", aa)
	su = 0
	for a in aa:
		a = int(a)
		if a in squareBank:
			su += squareBank[a]
		else:
			tem = a * a
			squareBank[a] = tem
			su += tem
	# print("Sum of aa ", su)
	return su

cases = int(input())
for cas in range(cases):	
	N = int(input())
	found = False
	rangeit = decideRange(N)
	# print("range is", rangeit)

	for i in range(rangeit[0], rangeit[1] + 1, 1):
		if itDosentHasZeros(i):
			bigSquare = getSumOfSquare(list(str(i)))
			if isPerfectSquare(bigSquare):
				print(i)
				found = True
				break

	if found == False:
		print(-1)

	# print(squareBank)

'''
1 - 9
10 - 99
100 - 999
1000 - 9999
10000 - 99999
'''