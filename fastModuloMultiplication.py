import math
def fast_exp(base, n):

	# base case
	if (n == 0):
		return 1

	if (n % 2 != 0):
		# Even
		return base * fast_exp(base*base, ((n - 1) / 2) )

	else:
		# Odd
		return fast_exp(base*base, (n / 2))



def sansar():
	
	base = 3
	n = 10

	ans = fast_exp(base, n)
	print(ans)



sansar()