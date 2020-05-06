# Question​ : Write a function that returns all permutations of a given list

def permute22(start, arr):
	for i in range(start, arr):
		# swap
		# recursefor next element
		# backtrack

		print(arr[i])


def permute33(arr):
	for i in range(len(arr)):
		for j in  range(i, len(arr)):
			t = arr[j]
			arr[j] = arr[i]
			arr[i] = t
			print(''.join(arr))
			t = arr[j]
			arr[j] = arr[i]
			arr[i] = t
			# print(arr[j], end="")
		print()

def magic(arr):
	print(''.join(arr))

def permute323(begg, arr, ans):
	if begg+1 == len(arr):
		ans.append(''.join(arr))
		return

	for i in range(begg, len(arr)):
		t = arr[begg]
		arr[begg] = arr[i]
		arr[i] = t
		permute323(begg+1, arr, ans)
		t = arr[begg]
		arr[begg] = arr[i]
		arr[i] = t
	return ans

stree = "ubuntu"
arr = list(stree)
ans = permute323(0,arr, [])
print(ans)