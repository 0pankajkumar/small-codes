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

def itDosentHasZeros(p, q):
	s = str(p) + str(q)
	ct = s.count('0')
	return True if ct == 0 else False

def getFirstNDigitNumber(triplet, N):
	a = triplet[0]
	b = triplet[1]
	found = False
	i = 1

	while (found == False):
		p = a * i
		q = b * i
		i += 1
		tem = ()
		print(p, q)

		totalNumberOfDigits = combineNosCountDigits(p, q)
		if totalNumberOfDigits == N:
			if itDosentHasZeros(p , q):
				found = True
				print("It doesnt has zeros")
				tem = (p, q)
				return (p, q)
			else:
				found = False
		elif totalNumberOfDigits > N:
			return () 
			
	return tem

def glue(g):
	if len(g) != 0:
		return int(str(g[0]) + str(g[1]))



cases = int(input())
for cas in range(cases):	
	N = int(input())

	# Get first N digit a, b from (3,4,5)
	f = getFirstNDigitNumber((3,4,5), N)

	# Get first N digit a, b from (5,12,13)
	g = getFirstNDigitNumber((5,12,13), N)

	print("Here come f g", f, g)

	# Pick the smallest of the two
	# Join those two numbers as string and print

	f = glue(f)
	g = glue(g)

	if f is None:
		print(g)
	else:
		if g is None:
			print(f)
		elif f < g:
			print(f)
		else:
			print(g)

	


















# (11, 60, 61),
# 		(19, 180, 181),
# 		(29, 420, 421),
# 		(59, 1740, 1741),
# 		(61, 1860, 1861),
# 		(71, 2520, 2521),
# 		(79, 3120, 3121),