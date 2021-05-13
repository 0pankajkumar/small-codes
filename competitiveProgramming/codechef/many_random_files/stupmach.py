import sys  
sys.stdin = open('input.txt', 'r') 

'''
Author : pankaj2kumar@codechef
'''

def getMin(arr):
	mini = arr[0]
	index = 0
	for i in range(len(arr)):
		if arr[i] < mini:
			mini = arr[i]
			index = i
	return mini,index

def solve1(n,arr):
	ans = 0
	asum = 0


	while len(arr) > 1:
		mini, index = getMin(arr)
		ans += ((mini-asum) * len(arr))
		asum += mini - asum
		arr = arr[:index]
		# if index == 0:
		# 	break


	print(ans+arr[0]-asum)

def solve2(n,arr):
	ans = arr[0]
	x = arr[0]
	for i in range(1,n):
		x = min(arr[i], x)
		ans += x

	print(ans)

for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	
	solve2(n,arr)



	



