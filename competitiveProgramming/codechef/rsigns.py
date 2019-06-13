cases = int(input())

def splitting(str):
    return [w for w in str]

for cas in range(cases):
	K = int(input())
	K = 10 ** K
	count = 0

	for i in range(K):
		num = i
		num1 = i
		a = splitting(str(num))
		mySet = set()
		for j in a:
			mySet.add(j)

		num = K - num - 1
		a = splitting(str(num))
		for j in a:
			mySet.add(j)

		if len(mySet) == 2:
			count += 1
			# print(f"{num1}, {num}")
			# print("~")

	print(count)