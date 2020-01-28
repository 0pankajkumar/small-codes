# your code goes here
import sys
sys.stdin = open('input.txt', 'r')




k, n = map(int, input().split())

bank = [0] * (k+1)
count = 0

for _ in range(n):
	
	temp = input()
	if temp == "CLOSEALL":
		count = 0
		bank = [0] * (k+1)
	
	else:
		s, p = temp.split()
		p = int(p)
		
		if bank[p] == 0:
			bank[p] = 1
			count += 1
		else:
			bank[p] = 0
			count -= 1
		
	print(count)
	