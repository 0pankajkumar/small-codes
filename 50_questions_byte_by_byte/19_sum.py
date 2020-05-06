'''
Question​ : Given two integers, write a function to sum the numbers without using any
arithmetic operators
'''

def sumWithoutPlus(a,b):
	if b==0:
		return a
	while b>0:
		partially = a ^ b
		carry = (a & b) << 1
		b = carry
		a = partially
	return partially

print(sumWithoutPlus(210,12))