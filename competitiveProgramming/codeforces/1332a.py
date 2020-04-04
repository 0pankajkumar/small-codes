import sys
sys.stdin = open("input.txt", 'r')

def check(p,q, x1,y1, x2,y2):
	# p, q is coord to be checked
	if p >= x1 and p <= x2:
		if q >= y1 and q <= y2:
			return True
		else:
			return False

for ssss in range(int(input())):
	a,b,c,d = map(int, input().split())
	x,y, x1,y1, x2,y2 = map(int, input().split())

	# left, right, down, up
	hturns = 0
	vturns = 0

	goHori = True
	goVerti = False

	while a+b+c+d > 0:
		if goHori:
			# print("---")
			if a > 0:
				if check(x-1,y, x1,y1, x2,y2):
					a -= 1
				hturns += 1
			if b > 0:
				if check(x+1,y, x1,y1, x2,y2):
					b -= 1
				hturns += 1
			if a == 0 and b == 0:
				goVerti = True
				goHori = False

		if goVerti:
			# print("^^^")
			if c > 0:
				if check(x,y-1, x1,y1, x2,y2):
					c -= 1
				vturns += 1
			if d > 0:
				if check(x,y+1, x1,y1, x2,y2):
					d -= 1
				vturns += 1
			if c == 0 and d == 0:
				goVerti = False
				goHori = False

		if goVerti is False and goHori is False:
			break
		if hturns > abs(x1) + abs(x2) + 10:
			print("breakiig beacuse of hturms")
			break
		if vturns > abs(y1) + abs(y2) + 10:
			print("breakiig beacuse of vturms")
			break

	if a == 0 and b == 0 and c ==0 and d == 0:
		print("Yes")
	else:
		print(a,b,c,d)
		print("No")
