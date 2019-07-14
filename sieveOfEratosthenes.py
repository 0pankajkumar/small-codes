#seive of Eratosthenes
#Getting prime numbers with a range

import math

n = 1000

arr = [0]*n
arr[0] = -1
arr[1] = -1
p = 1

# 1 is crossed
# 0 is still uncrossed
for _ in range(2,math.ceil(math.sqrt(n))):

	p += 1
	i = 1
	if arr[p] == 0:

		while p*i < n:
			#print("Yeah")
			arr[p*i] = 1
			i += 1
		arr[p] = 0
		#print(arr)
	else:
		continue

ans = []
for i in range(len(arr)):
	if arr[i] == 0:
		ans.append(i)
print(ans)