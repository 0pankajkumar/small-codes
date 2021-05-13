import sys
sys.stdin = open('input.txt', 'r')

for testcases in range(int(input())):
	n = int(input())
	brr = list(map(int, input().split()))
	grr = list(map(int, input().split()))
	brr.sort()
	grr.sort()
	line = list()
	flatNo = False

	if brr[0] < grr[0]:
		line.append(brr[0])
		i = 1
		j = 0
		toggle = False
		curr = -999999999

		while i < n or j < n:
			if toggle is False:
				if curr > grr[j]:
					flatNo = True
					break
				curr = grr[j]
				j += 1
				line.append(curr)
				toggle = True
			else:
				if curr > brr[j]:
					flatNo = True
					break
				curr = brr[i]
				i += 1
				line.append(curr)
				toggle = False
	else:
		line.append(brr[0])
		i = 0
		j = 1
		toggle = False
		curr = -999999999

		while i < n or j < n:
			if toggle is True:
				if curr > grr[j]:
					flatNo = True
					break
				curr = grr[j]
				j += 1
				line.append(curr)
				toggle = False
			else:
				if curr > brr[j]:
					flatNo = True
					break
				curr = brr[i]
				i += 1
				line.append(curr)
				toggle = True

	# print(line)
	if flatNo:
		print("NO")
		continue
	prev = -1
	for a in line:
		if prev > a:
			print("NO")

	print("YES")

