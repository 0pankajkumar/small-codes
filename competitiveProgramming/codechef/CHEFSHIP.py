import sys
sys.stdin = open('input.txt', 'r')

def balance(candid):
	l = len(candid)
	if l%2 != 0:
		return False
	a = candid[:l//2]
	b = candid[l//2:]
	
	if a==b:
		return True
	else:
		return False

for sss in range(int(input())):
	# stree = list(input())
	stree = input()

	count = 0

	for i in range(2, len(stree),2):
		yin = stree[:i]
		yan = stree[i:]

		if balance(yin) and balance(yan):
			count += 1

	print(count)
		