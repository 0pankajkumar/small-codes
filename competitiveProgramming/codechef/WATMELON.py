import sys
sys.stdin = open('input.txt', 'r')

for testcases in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	su = sum(arr)

	print("YES" if su >= 0 else "NO")

	# i = len(arr)
	# while su > 0 and i > 0:
	# 	if len(arr) > su:
	# 		if i-1 > 0:
	# 			if arr[i-1] > 0:
	# 				su -= su
	# 	else:
	# 		su -= i
	# 		i -= 1


	# if su == 0:
	# 	print("YES")
	# 	continue
	# else:
	# 	print("NO")



















	# possible = False
	# for i in range(len(arr), 0, -1):
	# 	if i-1 >= 0:
	# 		if arr[i-1] > 0:
	# 			su -= i
	# 		elif arr[i-1] > 0:
	# 			su += i
	# 	if su == 0:
	# 		possible = True
	# 		break

	# if possible:
	# 	print("YES")
	# else:
	# 	print("NO")
