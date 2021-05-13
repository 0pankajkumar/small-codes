import sys
sys.stdin = open('input.txt', 'r')

r, c, n = map(int, input().split())
xCor = list()
yCor = list()
for i in range(n):
	a,b = map(int, input().split())
	xCor.append(a)
	yCor.append(b)


max(xCor)
max(yCor)
print(xCor, yCor)


"""

Ditching problem midway as Codechef is not responding to submitted answers
It's taking forever to get AC, TLE or WA

"""
