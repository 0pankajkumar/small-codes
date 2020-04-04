# your code goes here
from collections import defaultdict
import sys
# sys.stdin = open('input.txt', 'r') 

for _ in range(int(sys.stdin.readLine())):
	n, q = map(int, sys.stdin.readLine().split())
	a = list(map(int, sys.stdin.readLine().split()))
	
	dic = defaultdict(int)
	
	for e in a:
		if bin(e).count('1') % 2 == 0:
			dic['even'] += 1
		else:
			dic['odd'] += 1
	
	for i in range(q):
		p = int(sys.stdin.readLine())
		
		if bin(p).count('1') % 2 == 0:
			print(dic['even'], dic['odd'])
		else:
			print(dic['odd'], dic['even'])
		