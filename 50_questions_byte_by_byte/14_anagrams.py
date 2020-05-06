
def isAnagram(st1, st2):
	bank=dict()
	for s in st1:
		s = s.lower()
		if s not in bank:
			bank[s] = 1
		else:
			bank[s] += 1

	for s in st2:
		s = s.lower()
		if s not in bank:
			return False
		else:
			bank[s] -= 1

	for k,v in bank.items():
		if v != 0:
			return False

	return True

st1 = "AB"
st2 = "ab"
print(isAnagram(st1, st2))
