'''
Question​ : Given two integers, write a function to determine whether or not their binary
representations differ by a single bit.
'''
import math

def gray(a,b):
	x = a^b
	k = math.log(x,2)

	if int(k) == k:
		return True
	else:
		return False

print(gray(1,2))
