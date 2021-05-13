import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')

def check(p):
	co = 0
	for i in range(len(p)):
		if i+1 < len(p):
			if p[i] == p[i+1]:
				co += 1
	return co

from itertools import permutations
for _ in range(int(input())):
	s = input()
	permList = permutations(s)

	count = 0
	for p in list(permList):
		print(p)
		m = check(p)
		print(m)
		count += m

	print(count)
