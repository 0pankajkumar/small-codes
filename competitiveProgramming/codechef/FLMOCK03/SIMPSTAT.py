import sys, math  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')  

def flip(s, start, end):
	for i in range(start, end + 1):
		s[i] = 'R' if s[i] == 'G' else 'G'

for t in range(int(input())):
	n, k = map(int, input().split())
	s = [False]
	temp = list(input())
	s.extend(temp)

	count = 0
	for i in range(1, n+1):
		if s[i] == 'R':
			flip(s, i, min(n, i + k - 1))
			count += 1
	# print(''.join(s[1:]))
	print(count)