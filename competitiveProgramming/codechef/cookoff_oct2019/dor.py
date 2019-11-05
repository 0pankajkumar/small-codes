
cases = int(input())

for cas in range(cases):

	n, m = map(int, input().split())

	ans = n | n + 1

	for i in range(n + 1, m + 1):
		ans = ans | i 

	print(ans)


