# import sys  
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')

for t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	flag = False
	diff = 0
	pri = "YES"

	if n == 1:
		if a[0] != b[0]:
			pri = "NO"
	else:
		for i in range(n):
			if a[i] != b[i] and flag is False:
				tw = a[i] - b[i]
				diff = tw if tw > 0 else -1 * tw
				flag = True
			elif a[i] == b[i]:
				continue
			else:
				tw = a[i] if a[i] < b[i] else b[i]
				if tw + diff != b[i]:
					pri = "NO"
					break

	print(pri)

