# your code goes here
import sys
sys.stdin = open('input.txt', 'r')

for _ in range(int(input())):
	p = int(input())
	n = p * p
	brr = [[0]*p]*p
	
	i = 1
	limiter = 0
	
	while i < n:
		k = limiter
		for j in range(0, limiter+1):
			brr[j][k] = i
			if k != 0:
				k -= 1
			else:
				break
			if i+1 < n:
				i += 1
			else:
				break
		if limiter+1 < p:
			limiter += 1
			
	print(brr)