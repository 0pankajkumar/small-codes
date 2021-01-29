import sys
sys.stdin = open('input.txt', 'r')

seven = '7'

def eliminate(n, b):

	if seven in n:
		position = n.index(seven)
		revPosition = len(n) - position - 1

		t = int(n)
		t -= (10**revPosition)
		n = str(t)
		b += 10**revPosition
		# print(revPosition)
	else:
		return n,b

	return eliminate(n, b)


for testcases in range(int(input())):
	n = input()
	a, b = eliminate(n, 0)
	print(a,b)
