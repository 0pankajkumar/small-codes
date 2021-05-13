import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


cases = int(input())

for cas in range(cases):
	n = int(input())
	arr = list(map(int, input().split()))

	prev = arr[0]
	for i in range(1, len(arr)):
		if prev+1 == arr[i]:
			# continue
		else:
			# append the number























'''
def sendForPacking(a, b):
	return str(a) + "..." + str(b)
# your code goes here
cases = int(input())

for cas in range(cases):
	n = int(input())
	arr = list(map(int, input().split()))

	ans = list()
	started = "no"
	justEnded = "no"
	prev = arr[0]

	for i in range(len(arr)):
		if arr[i] == prev+1:
			if started is "no":
				pack_i = i-1
				started = "yes"
			if started is "yes":
				pack_j = i
				justEnded = "yes"
		elif justEnded is "yes":
			started = "no"
			ans.append(sendForPacking(arr[pack_i], arr[pack_j]))
		else:
			ans.append(str(arr[i]) + ',')

	print(''.join(ans))
'''
























'''
# your code goes here
cases = int(input())

for cas in range(cases):
	n = int(input())
	arr = list(map(int, input().split()))
	ans = list()

	try:
		prevprev = (arr[0])
		prev = (arr[1])
		ans.append(prev)
		flag = False
	except:
		prevprev = -3
		prev = (arr[0])
		ans.append(prev)
		flag = False

	for i in range(2, n):
		if (prevprev+1) == prev and (prev+1) == arr[i] and flag is False:
			ans.append('...')
			flag = True
		else:
			ans.append(str(arr[i]))
			ans.append(',')
		prevprev = (prev)
		prev = (arr[i])

	print(''.join([str(a) for a in arr]))
'''






'''
def sendForPacking(l, ans):
	if len(l) <= 2:
		# Comma
		for q in l:
			ans.append(str(q))
			ans.append(',')
	else:
		# Dot
		ans.append(str(l[0]))
		ans.append("...")
		ans.append(str(l[-1]))
		ans.append(',')
	# ans.append(',')

for cas in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))

	if n == 1:
		print(arr[0])
	else:
		prev = arr[0]
		ans = list()
		arr = arr[1:]
		l = [prev]
		for i in range(len(arr)):
			if prev+1 == arr[i]:
				l.append(arr[i])
				prev = arr[i]
				if arr[i] == arr[-1]:
					sendForPacking(l, ans)
			elif len(l) >= 2:
				sendForPacking(l, ans)
				l = list()
				l.append(arr[i])
				prev = arr[i]
				if arr[i] == arr[-1]:
					sendForPacking(l, ans)
			else:
				if i+1 < len(arr):
					if arr[i+1] != arr[i]+1:
						l.append(arr[i])
						prev = arr[i]
						sendForPacking(l, ans)
						l = list()
					else:
						l.append(arr[i])
						prev = arr[i]
				else:
					l.append(arr[i])
					prev = arr[i]
					sendForPacking(l, ans)
					l = list()

		# if len(l) != 0:
		#   sendForPacking(l, ans)
		ans = ans[:-1]
		print(''.join(ans))
'''
