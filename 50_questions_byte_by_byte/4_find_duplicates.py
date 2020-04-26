'''
Question​ : Given an array of integers where each value 1 <= x <= len(array), write a
function that finds all the duplicates in the array.
'''

def dups(arr):
	bank = set()

	for i in range(len(arr)):
		if arr[abs(arr[i])-1] < 0:
			bank.add(abs(arr[i]))
		else:
			arr[abs(arr[i])-1] = -1*arr[abs(arr[i])-1]
	for i in range(len(arr)):
		arr[i] = abs(arr[i])
	return list(bank)

arr1 = [2,1,2,1]
print(dups(arr1))
