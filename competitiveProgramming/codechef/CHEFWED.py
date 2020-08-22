# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

import sys
sys.setrecursionlimit(1500)

family = list()
cache = dict()
n = 0
k = 0

def initialize_cache():
	for i in range(n):
		cache[i] = -1

def dp(l):
	# print(f"dp called with {l}")
	if l >= n:
		return 0

	ans = cache[l]

	if cache[l] != -1:
		return cache[l]

	cache[l] = 1e8

	tempDict = dict()
	g = 0
	temp = 0
	endNumber = 0

	for i in range(l,n):
		if family[i] in tempDict:
			if tempDict[family[i]] == 1:
				temp += 1

		if family[i] in tempDict:
			tempDict[family[i]] += 1
		else:
			tempDict[family[i]] = 1

		if family[i] in tempDict:
			if tempDict[family[i]] > 1:
				g += 1

		endNumber = k if i+1 < n else 0
		# print(endNumber)

		cache[l] = min(cache[l], g + temp + endNumber + dp(i+1)) 

	return cache[l]


for sss in range(int(input())):
	try:
	    n, k = map(int, input().split())
	    family.clear()
	    family = list(map(int, input().split()))

	    cache = dict()
	    initialize_cache()

	    ans = k + dp(0)
	    # print(cache)
	    print(ans)
	except:
		pass
