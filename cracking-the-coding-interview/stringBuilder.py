
def stringBuilder(arr):
	"""
	Mimics the String builder of Java type languages
	args:
		An array of strings
	returns:
		A concatenated string of all strings
	"""
	masterList = list()
	for a in arr:
		t = list(a)
		masterList.extend(t)

	return ''.join(masterList)


arr = ["jumper", "jackets", "are", "cool"]
concat = stringBuilder(arr)
print(concat)
