
import sys
sys.stdin = open("input.txt", 'r')


def getDivisors(n, bank) : 
	i = 1
	while i <= math.sqrt(n): 
		if (n % i == 0):
			bank.add(n/i)
			bank.add(i)
		i = i + 1

def solver1():
	for ssss in range(int(input())):
		x,k = map(int, input().split())

		bank = set()
		getDivisors(x,)


def handle():
	solver1()

handle()