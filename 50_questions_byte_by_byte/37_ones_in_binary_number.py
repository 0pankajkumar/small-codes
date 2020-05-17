'''
Question​:Given an integer, write a function to compute the number of ones in the binary
representation of the number.
'''

def ones(n):
	cou = 0
	while n:
		right_most_digit = n % 2
		if right_most_digit ^ 0b1 == 0:
			cou += 1
		n >>= 1
	return cou

n = 7
ans = ones(n)
print(ans)