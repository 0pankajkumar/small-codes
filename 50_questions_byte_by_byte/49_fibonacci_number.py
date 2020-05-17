# Question​ : Given an integer n, write a function to compute the nth Fibonacci number.

def fibo(n):
	if n <= 1:
		return n
	a=0
	b=1
	while n>1:
		f = a+b
		a=b
		b=f
		n-=1

	return f

n = 109252
ans = fibo(n)
print(ans)