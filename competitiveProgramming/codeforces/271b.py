import sys
sys.stdin = open("input.txt", 'r')

# Make prime numbers
maxim= 100005
prime = [True] * maxim
prime[0] = False
prime[1] = False
for i in range(2,maxim):
	if prime[i]:
		for j in range(i+i, maxim,i):
			prime[j] = False

n,m = map(int, input().split())
rows = [0]*n
cols = [0]*m

for i in  range(n):
	arr = list(map(int, input().split()))
	for j in range(m):
		x = arr[j]
		while not prime[x]:
			x+=1
		rows[i] += (x-arr[j])
		cols[j] += (x-arr[j])

# print(rows)
# print(cols)
print(min(min(rows),min(cols)))



