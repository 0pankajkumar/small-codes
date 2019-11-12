# import sys  
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w') 

test = int(input())

for t in range(test):
	n, m = map(int, input().split())
	prr = list(map(int, input().split()))
	qrr = list(map(int, input().split()))
	result = [0] * (n + m - 1)

	for i in range(n):
		for j in range(m):
			result[i + j] += prr[i] * qrr[j]
			# print("i, j, result ",i , j, result[i + j])

	for r in result:
		print(r, end=" ")
	print()



