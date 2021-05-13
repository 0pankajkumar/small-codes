import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')  


for t in range(int(input())):
	n, q = map(int, input().split())
	nrr = list(map(int, input().split()))
	
	for qq in range(q):
		k = int(input())
		ncpy = nrr.copy()

