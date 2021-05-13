import sys
sys.stdin = open("input.txt", 'r')

for rrr in range(int(input())):
	n = int(input())
	st = input()

	x = 0
	y = 0
	curr = None

	for s in st:
		if (s == 'L' or s == 'R') and (curr != 'L' and curr != 'R'):
			if s == 'L':
				curr = 'L'
				x -= 1
			elif s == 'R':
				curr = 'R'
				x += 1
		elif (s == 'U' or s == 'D') and (curr != 'U' and curr != 'D'):
			if s == 'U':
				curr = 'U'
				y += 1
			elif s == 'D':
				curr = 'D'
				y -= 1

	print(x, y)
