
import sys  
sys.stdin = open('input.txt', 'r') 

def solve22(a, b, x, y, n):
	"""greedy towards a then b"""


	minuser = x if (a-x) >= n else (a-x)
	a -= minuser

	n -= minuser

	minuser = y if (b-y) >= n else (b-y)
	b -= minuser

	return a*b
	
def solve2(a,b,x,y,n):
	ans1 = solve(a, b, x, y, n)
	ans2 = solve(b, a, y, x, n)
	print("answers ",ans1,ans2)
	ans = min(ans1, ans2)
	print(ans)

def solve3(a,b,x,y,n):
	if (a-x > b-y):
		if(a-x < n):
			a -= (a-x)
			n -= (a-x)
			if (b-y < n):
				b -= (b-y)
				n -= (b-y)
			elif(b-y > n):
				b -= n
				n -= n

		elif(a-x >= n):
			a -= n
			n -= n

	else:
		if (b-y < n):
			b -= (b-y)
			n -= (b-y)
		elif(b-y >= n):
			b -= n
			n -= n

	return a*b

def solve44(a,b,x,y,n):
	minuser = min(a-x, n)
	a -= minuser
	n -= minuser

	minuser = min(b-y, n)
	b -= minuser
	n -= minuser

	return a*b

def solve4(a,b,x,y,n):
	return (min(solve44(a,b,x,y,n), solve44(b,a,y,x,n)))

for testcases in range(int(input())):
	a, b, x, y, n = map(int, input().split())
	print(solve4(a,b,x,y,n))