import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output2.txt', 'w')  


test = int(input())

for t in range(test):
	n, q = map(int, input().split())
	nrr = list(map(int, input().split()))
	qrr = list(map(int, input().split()))

	j = 0
	k = 0
	maxx = nrr[0]
	for i in range(len(nrr)):
		if nrr[i] > maxx:
			maxx = nrr[i]
		if i + 1 == qrr[k]:
			qrr[k] = maxx
			k += 1

	for qr in qrr:
		print(qr)


