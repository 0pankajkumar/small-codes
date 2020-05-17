'''
Question​ : Given an array containing all the numbers from 1 to n except two, find the two
missing numbers
'''


def missing(arr, n):
	bank = set()
	su = 0
	req_su = 0

	# Making a sum array & set
	for a in arr:
		su += a
		bank.add(a)

	# Sum of natural numbers
	for i in range(1,n+1):
		req_su += i

	# Determining sum of those two missing numbers
	twoSum = req_su - su

	# trying to generate combinations
	for i in range(1,(n//2)+1):
		if i not in bank:
			if twoSum-i not in bank:
				return i, twoSum-i

	return None, None

arr = [4,2,3]
a,b = missing(arr, len(arr)+2)
print(a,b)