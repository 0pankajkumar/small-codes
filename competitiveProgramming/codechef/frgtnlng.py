
cases = int(input())
for cas in range(cases):
	n, k = map(int, input().split())
	frg = input().split()

	found = ["NO"] * n

	for kk in range(k):
		phr = input().split()
		phr = phr[1:]

	i = 0
	for p in phr:
		if p == frg[i]:
			found[i] = "YES"
		if i < len(frg) - 1:
			i += 1
				
	print(found)




