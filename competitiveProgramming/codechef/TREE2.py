for testcases in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	s = set(arr)

	if 0 in s:
		print(len(s)-1)
	else:
		print(len(s))