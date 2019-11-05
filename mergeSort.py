# merge sort
import math
def merge(left, right, A):
	# Merge & send a list back
	# if not left:
	# 	if not right:
	# 		return
	# 	else:
	# 		return right

	i = j = k = 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			A[k] = left[i]
			i += 1
			k += 1
		else:
			A[k] = right[j]
			j += 1
			k += 1


	while i < len(left):
		A[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		A[k] = right[j]
		j += 1
		k += 1


def mergeSort(A):
	# Base case
	print(A)
	if len(A) < 2:
		return

	#Divide into two halves
	nA = len(A)
	nLeft = math.floor(nA / 2)
	nRight = nA - nLeft

	# Call for the first half
	left = mergeSort(A[:nLeft])

	# Call for the second half
	right = mergeSort(A[nRight:])

	# Merge left & right half
	return merge(left, right, A)



print(mergeSort([3,7,4,1,9,2]))