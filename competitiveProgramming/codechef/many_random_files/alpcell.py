# cook your dish here
cases = int(input())

for cas in range(cases):
	n,m = map(int, input().split())

	a = []
	for i in range(0, 26):
		a.append(0)

	for row in range(n):
		alphas = input()
		for i in alphas:
			a[ord(i) - 97] += 1

	print(chr(97 + a.index(max(a))))