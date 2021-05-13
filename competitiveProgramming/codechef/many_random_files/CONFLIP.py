import sys  
sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')

for t in range(int(input())):
	sss = int(input())
	while sss:
		l,n,q = map(int, input().split())

		if n%2 ==0:
			print(n//2)
		else:
			if l==q:
				print(n//2)
			else:
				print(n//2 + 1)

		sss-=1
	
	