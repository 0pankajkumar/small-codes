
import sys
sys.stdin = open("input.txt", 'r')


mo = 1000000007
def solver1():
	for ssss in range(int(input())):
		n = int(input())
		prr = list(map(int, input().split()))
		prr.sort(reverse=True)
		pocket = 0
		minus = -1
		for p in range(n):
			minus += 1
			if prr[p] != 0:
				if prr[p] - minus >= 0:
					prr[p] -= minus
					t = prr[p] % mo
					pocket += t
			# else:
			# 	break
		print(pocket % mo)

def solver2():
	for ssss in range(int(input())):
		n = int(input())
		prr = list(map(int, input().split()))
		prr.sort()

		# Removing all zeros
		for i in range(n):
			if prr[i] == 0:
				continue
			else:
				prr = prr[i:]
				break
		# print(prr)

		# Removing all smaller values
		for i in range(len(prr)):
			if prr[i] > n:
				prr = prr[i:]
				break

		pocket = sum(prr)
		k = 1
		for i in range(len(prr)-1):
			pocket -= k
			k += 1
		print(pocket % mo)


def handle():
	solver1()

handle()