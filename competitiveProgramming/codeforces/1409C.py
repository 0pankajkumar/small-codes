
import sys  
sys.stdin = open('input.txt', 'r') 

from collections import deque

def solve4(n,x,y):
	diff = y-x
	print(x, y, end=" ")
	for i in range(0, n-2	):
		print(y+diff ,end=" ")
		y += diff
	print()

def solve5(n,x,y):
	diff = y-x
	arr = deque()
	arr.append(y)
	xFound = False
	t = y

	while n > 0:
		n -= 1
		t -=diff
		if t <= 0:
			break	
		arr.appendleft(t)

		if t == x:
			xFound = True

	t = y
	while n > 0:
		t += diff
		arr.append(t)
		n -= 1



	print(arr)





for testcases in range(int(input())):
	n, x, y = map(int, input().split())
	solve5(n,x,y)