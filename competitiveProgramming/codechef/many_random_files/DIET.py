import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')

for t in range(int(input())):

	n, k = map(int, input().split())
	arr = list(map(int, input().split()))

	found = True
	bank = 0
	for i in range(n):
		cut = arr[i] - k
		bank += cut
		if bank < 0:
			print(f"NO {i+1}")
			found = False
			break

	if found is True:
		print("YES")

