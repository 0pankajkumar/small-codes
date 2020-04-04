# recursive dfs
import sys
sys.stdin = open("input.txt", 'r')
from collections import defaultdict

def dfs(cur, par):
	# print(cur)
	dp[cur] = wei[cur]
	zero = 0
	for child in g[cur]:
		if child == par:
			continue
		dfs(child, cur)
		zero = max(dp[child], zero)

	dp[cur] += zero

g = defaultdict(list)

n = int(input())
dp = defaultdict(lambda:0)

for ssss in range(n-1):
	a,b = map(int, input().split())
	g[a].append(b)
	g[b].append(a)

# wei = dict()
wei = list(map(int, input().split())) 
wei.insert(0,0)

dfs(1, 0)
print("ans", dp[1])