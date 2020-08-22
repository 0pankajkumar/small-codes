import sys
sys.stdin = open('input.txt', 'r')

for sss in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))

	bank = dict()
	flag = True
	curr = arr[0]

	for a in arr:
		if a in bank:
			if curr == a:
				bank[a] += 1
				continue
			else:
				flag = False
				# break
		else:
			bank[a] = 1
			curr = a
	
	flag2 = True
	bank2 = set()
	for k,v in bank.items():
		if v in bank2:
			flag2 = False
			break
		else:
			bank2.add(v)	

	if flag and flag2:
		print("YES")
	else:
		print("NO")