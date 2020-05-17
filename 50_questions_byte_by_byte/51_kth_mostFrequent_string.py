'''
Question​ : Given a list of strings, write a function to get the kth most frequently
occurring string
'''

# Assuming there is only one such string
def kth_most(arr, n):
	counterBank = dict() # A dict to hold all counts of alphabets
	reverseBank = dict() # A dict to reverse counterBank dict with key,value pairs swaped
	countsList = list() # A list of all counts so that we can sort the counts with ease
	for a in arr:
		if a not in counterBank:
			counterBank[a] = 1
		else:
			counterBank[a] += 1

	for k,v in counterBank.items():
		reverseBank[v] = k
		countsList.append(v)

	countsList.sort(reverse=True)

	try:
		ans = reverseBank[countsList[n]]
	except:
		ans = None

	print(ans)


dictionary = ['a','b','c','a','b','a']
kth_most(dictionary, 3)


