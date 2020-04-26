
import sys
sys.stdin = open("input.txt", 'r')


import operator as op
import math
from functools import reduce
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def getPrimeFactorsCount(x):
	count = 0
	while x%2 == 0:
		count += 1
		x /= 2

	for i in range(3,math.ceil(math.sqrt(x)),2):
		while x%i == 0:
			count += 1
			x /= i 
	if x > 1:
		count += 1
	return count

def solver2(x,k):
	# Editorial solution
	print(1 if getPrimeFactorsCount(x) >= k else 0)

def solver1(x,k):
	# if k > x:
	# 	return 0

	if k == 1:
		if x == 2:
			return 0
		else:
			return 1
	if k == 2:
		if x == 4:
			return 0
		else:
			return 1


	t = ncr(k,2)
	# print("t",t)
	if t >= (x-k-1):
		return 0
	else:
		return 1


def underTaker():
	for ssss in range(int(input())):
		x,k = map(int, input().split())
		solver2(x,k)



def handle():
	underTaker()

handle()