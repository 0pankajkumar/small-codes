import sys
sys.stdin = open('input.txt', 'r')

for _ in range(int(input())):
	n = int(input())
	brr = list()
	for i in range(n):
		price, quantity, discount = map(int, input().split())
		brr.append((price, quantity, discount))

	grandLoss = 0

	for b in brr:
		p = b[0]
		q = b[1]
		d = b[2]
		new_price = p
		new_price *= (1 + d / 100)
		new_price *= (1 - d / 100)
		loss = (p - new_price) * q
		grandLoss += loss

	print(grandLoss)

	
	# n, p, q = map(int, input().split())
	# arr = list(map(int, input().split()))
	
	