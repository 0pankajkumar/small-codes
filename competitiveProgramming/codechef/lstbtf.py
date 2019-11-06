import math
def combineNosCountDigits(a, b):
	count1 = 0
	while(a != 0):
		a = math.floor(a / 10)
		count1 += 1

	count2 = 0
	while(b != 0):
		b = math.floor(b / 10)
		count2 += 1
	return count1 + count2

def getFirstNDigitNumber(triplet, N):
	a = triplet[0]
	b = triplet[1]
	found = False
	i = 1

	while (found == False):
		a = a * i
		b = b * i
		if combineNosCountDigits(a, b) == N:
			found = True
			return (a, b)





cases = int(input())
for cas in range(cases):	
	N = int(input())

	# Get first N digit a, b from (3,4,5)
	f = getFirstNDigitNumber((3,4,5), N)

	# Get first N digit a, b from (5,12,13)
	g = getFirstNDigitNumber((5,12,13), N)

	print(f, g)

	# Pick the smallest of the two

	# If it contains zero loop & get the next non zero pair

	# Join those two numbers as string and print



















# (11, 60, 61),
# 		(19, 180, 181),
# 		(29, 420, 421),
# 		(59, 1740, 1741),
# 		(61, 1860, 1861),
# 		(71, 2520, 2521),
# 		(79, 3120, 3121),