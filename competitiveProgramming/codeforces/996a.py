# import sys
# sys.stdin = open("input.txt", 'r')

n = int(input())

# 1, 5, 10, 20, 100
bills = 0

while(n > 0):
	if n >= 100:
		bills += 1
		n -= 100
	elif n >= 20:
		bills += 1
		n -= 20
	elif n >= 10:
		bills += 1
		n -= 10
	elif n >= 5:
		bills += 1
		n -= 5
	elif n >= 1:
		bills += 1
		n -= 1

print(bills)