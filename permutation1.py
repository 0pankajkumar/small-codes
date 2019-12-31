
def allOptions(arr):
	if len(arr) <= 1:
		return [arr]
	else:
		a = arr[-1]
		options = allOptions(arr[:-1])
		permutations = []

		for opt in options:
			for i in range(len(arr)):
				first = opt[:i]
				last = opt[i:]
				permutations.append(first + [a] + last)
		return permutations




arr = list("123")
print(allOptions(arr))