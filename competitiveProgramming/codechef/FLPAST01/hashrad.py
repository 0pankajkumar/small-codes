import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output2.txt', 'w') 

def sumHash(ss):
	sumis = 0
	for s in ss:
		sumis += s
	return sumis

def carryOver(ss):
	carry = 1
	pos = len(ss) - 1
	while carry == 1:
		if ss[pos] < 25:
			ss[pos] += 1
			carry = 0
		else:
			ss[pos] -= 1
			carry = 1
		pos -= 1

test = int(input())

for t in range(test):
	ss = list(input())
	for i in range(len(ss)):
		ss[i] = ord(ss[i]) - ord('a')

	benchmark = sumHash(ss)
	found = False
	# print(ss)
	carryOver(ss)
	while sumHash(ss) != benchmark:
		carryOver(ss)
	# while(found == False):
	# 	carryOver(ss)
		# while sumHash(ss) != benchmark:
		# 	carryOver(ss)
		# if sumHash(ss) == benchmark:
		# 	found == True
	# print(ss)

	print(benchmark, end = " ")

	for s in ss:
		# print(s)
		print(chr(s + 97), end="")
	print()
