import sys  
sys.stdin = open('input.txt', 'r') 

'''
Author : pankaj2kumar@codechef
'''

for _ in range(int(input())):
	n,k = map(int, input().split())
	arr = list(map(int, input().split()))

	weights = 0
	count = 0
	flag = False

	for a in arr:
		if a > k:
			count = -1
			break

		weights += a

		if weights <= k:
			if flag is False:
				count += 1
				flag = True
		else:
			weights = a
			count += 1
			# flag = False


	if count == 0:
		print(-1)
	else:
		print(count)