# Brute force approch

# Receiving TLE on codechef
def smartMaxsIndex(W, i):

	if W[i] > W[i - 1]:
		return i
	else:
		return smartMaxsIndex(W[:-1], i - 1)


def allElementsAreNotSame(W):
	tem = W[0]
	# for w in W:
	# 	if w != tem:
	# 		return True
	if W[0] != W[-1]:
		return True
	return False

def IncrementMachine(W, scapegoat):
	for i in range(len(W)):
		if i != scapegoat:
			W[i] += 1

	# for i in range(scapegoat):
	# 	W[i] += 1
	# for i in range(scapegoat + 1, len(W), 1):
	# 	W[i] += 1

cases = int(input())
# cases = 1
for cas in range(cases):	
	N = int(input())
	W = list(map(int, input().split()))
	# W = [6, 7, 9, 13]
	# W.sort()

	scapegoat = len(W) - 1
	count = 0

	while(allElementsAreNotSame(W)):
		scapegoat = smartMaxsIndex(W, len(W) - 1)
		IncrementMachine(W, scapegoat)
		count += 1

	print(W, count)



'''
1. Make the highest element as scapegoat initially
2. Increment everything by 1 untill there is another element > scapegoat
3. Make that element as scapegoat
4. Check whether all elements are same
5. Repeat step 2


6 7 9 13
7 8 10 13
8 9 11 13
9 10 12 13
10 11 13 13
11 12 14 13
12 13 14 14
13 14 15 14
14 15 15 15
15 16 16 15
16 17 16 16
17 17 17 17

35 - 4*6 = 11
'''




import math
# pyhton code
s = '100'

# 0 = (2^0 * 0)
# 0 = ()

# for i in range(len(s) - 1, 1, -1):

i = 0
totSum = 0
while(len(s) != 0):
	temp = s[-1]

	p = math.pow(2,i) * int(temp)

	totSum += p 

	i += 1

print(totSum)














