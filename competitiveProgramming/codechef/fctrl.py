# your code goes here

import sys
sys.stdin = open("input.txt", 'r')

bank2 = dict()
bank5 = dict()

def get2n5(n):
	two = 0
	five = 0
	while n % 2 == 0:
		two += 1
		n /= 2
	
	while n % 5 == 0:
		five += 1
		n /= 5
		
	return two, five

def getZeros(n):
	tw = 0
	fi = 0
	while n > 1:
		two, five = get2n5(n)
		# bank2[n] = two
		# bank5[n] = five
		tw += two
		fi += five
		n -= 1
	
	print("Finised getting zeros")
	t = min(tw,fi)
	return t
	# zee = pow(10,t)
	# zee = str(zee)
	# return zee.count('0')
	
	
	
for ssss in range(int(input())):
	n = int(input())
	ans = getZeros(n)
	print(ans)