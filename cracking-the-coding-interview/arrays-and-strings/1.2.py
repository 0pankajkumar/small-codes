"""
Check Permutation: Given two strings, write a method to decide
 if one is a permutation of the other.
"""

a = "one"
b = "eno"


def checkWhetherPermutation(a,b):
	if len(a) != len(b):
		return False

	bank = dict()

	for ele in a:
		if ele not in bank:
			bank[ele] = 1
		else:
			bank[ele] += 1

	# Checking for being a permuation of the other
	for ele in b:
		if ele not in bank:
			return False
		else:
			bank[ele] -= 1
			if bank[ele] < 0:
				return False

	flag = "notok"
	for k,v in bank.items():
		if v > 0:
			flag = "ok"

	return True if flag == "notok" else False


print(checkWhetherPermutation(a,b))