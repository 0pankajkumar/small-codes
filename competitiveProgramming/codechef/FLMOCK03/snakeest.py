import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')  


for t in range(int(input())):
	n, q = map(int, input().split())
	nrr = list(map(int, input().split()))
	nrr.sort()
	
	for qq in range(q):
		k = int(input())
		arr = nrr.copy()
		count = 0
		eaten = 0

		for i in range(n - 1, -1, -1):
			currentEater = arr[i]
			if arr[i] >= k:
				count += 1
				
			elif eaten + currentEater >= k:
				count += 1
				eaten = 0
			else:
				eaten += 1


