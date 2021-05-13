
import sys
sys.stdin = open("input.txt", 'r')


def solver11():
	for ssss in range(int(input())):
		n = int(input())
		arr = list(map(int, input().split()))

		i = 0
		humanFound = False
		humanFoundAgain = False
		violated = False
		dist = 0

		while i < n:
			if arr[i] == 1:
				if humanFound is True:
					humanFoundAgain = True
				humanFound = True
				if humanFoundAgain is True and dist < 5:
					violated = True
					# print("i is",i)
					break
				else:
					humanFoundAgain = False
					dist = 0
			else:
				dist += 1
			i += 1

		print("NO" if violated else "YES")



def handle():
	solver11()

handle()