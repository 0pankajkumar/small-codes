import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')

for e in range(int(input())):
	h, w = map(int, input().split())
	bank = list()
	for ee in range(h):
		bank.append(list(input()))
		
	print(bank)
	
	