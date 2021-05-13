

cases = int(input())
# cases = 1
for cas in range(cases):	
	N = int(input())
	W = list(map(int, input().split()))
	
	ans = sum(W) - N * min(W)

	print(ans)