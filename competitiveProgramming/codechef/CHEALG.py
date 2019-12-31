import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')

for _ in range(int(input())):
	s = input()
	# aaabb
	b = ''
	ans = list()
	count = 0
	for a in s:
		if a == b:
			count += 1
			ans[-1] = str(count)
		else:
			b = a
			count = 1
			ans.append(a)
			ans.append('1')
	ans = ''.join(ans)

	print("YES" if len(s) > len(ans) else "NO")
	# print(''.join(ans))
	# print(len(s), len(ans))
