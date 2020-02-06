# your code goes here
import sys
sys.stdin = open('input.txt', 'r')

def bigger(a,b):
	a_bigger = False
	b_bigger = False
	
	if a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2]:
		a_bigger = True
	else:
		b_bigger = True
		
	return True if a_bigger else False
			

for _ in range(int(input())):
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	c = list(map(int, input().split()))
	
	exists = False
	
	if bigger(a,b):
		if bigger(a,c):
			# a is biggest
			exists = True
		elif bigger(c,b):
			# c is biggest,
			# a is bigger,
			# b is big
			exists = True
		else:
			exists = False
	else:
		if bigger(a,c):
			# b is biggest,
			# a is bigger,
			# c is big
			exists = True
		elif bigger(b,c):
			# b is biggest
			# c is bigger
			# a is big
			exists = True
		else:
			exists = False
			
	print("yes" if exists is True else "no")
			
			