import sys
sys.stdin = open("input.txt", 'r')

from collections import defaultdict
n = int(input())
g = defaultdict(list)
startingPoint = None
dp = defaultdict(str)

g[""] = ""
maxi = [0]

def dfs(ele, par):
	# print(ele)
	dp[ele] = 1
	zero = 0
	for e in g[ele]:
		if e == par:
			continue
		dfs(e, ele)
		zero = max(zero, dp[e])
	dp[ele] += zero
	maxi[0] = max(maxi[0], dp[ele])

for i in range(n):
	repost = list(input().split())
	repost[0] = repost[0].lower()
	repost[-1] = repost[-1].lower()
	g[repost[0]].append(repost[-1])
	g[repost[-1]].append(repost[0])

	if i == 0:
		startingPoint = repost[-1]

dfs(startingPoint, "")
# print(dp)
print(maxi[0])

