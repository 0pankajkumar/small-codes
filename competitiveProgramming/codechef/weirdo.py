# your code goes here
import math
def isStringBalanced(ss):
	# return true if string has equal nuber of vowel & consonents
	
	if(len(ss) <= 1):
		return True

	vowels = {'a' : True, 'e': True, 'i': True, 'o': True, 'u': True}
	vow = 0
	cons = 0
	
	for s in ss:
		if s in vowels:
			vow += 1
		else:
			cons += 1
			
	if vow >= cons:
		return True
	else:
		return False

def isBal(str, firstLove):
	
	if len(str) == 1:
		return True
	elif firstLove == True:
		return isStringBalanced(str) and isBal(str, False)
	else:
		return isStringBalanced(str[:-1]) and isBal(str[:-1], False)

def classify(array):
	# True if Alice's string
	# False otherwie
	alice = []
	bob = []

	for i in range(len(array)):
		if isBal(array[i], True):
			print("is true")
			alice.append(array[i])
			print("appended maybe", alice)
		else:
			print("is not true")
			bob.append(array[i])
			
	return alice, bob
def formSignature(signature, a, newWord):
	# Forms a dict signature in O(n) time
	# a is a string
	for s in a:
		if s in signature:
			signature[s]['totalCountOfX'] += 1
			if newWord:
				signature[s]['countOfWordsWhichContain'] += 1
				newWord = False
		else:
			signature[s] = dict()
			signature[s]['totalCountOfX'] = 1
			signature[s]['countOfWordsWhichContain'] = 1
			newWord = False

def calScore(array):
	# calculates score
	K = len(array)
	score = 1
	signature = dict()

	for a in array:
		#  True as newWord is passed to count countOfWordsWhichContain
		formSignature(signature, a, True)

	print("\n")
	print(signature)
	print("\n")

	for keys, values in signature.items():
		score *= (signature[keys]['countOfWordsWhichContain'] / math.pow(signature[keys]['totalCountOfX'], K))
	
	return score		




cases = int(input())
 
for cas in range(cases):
	array = []
	L = int(input())
	for l in range(L):
		array.append(input())
		
	alice, bob = classify(array)
	
	aliceScore = calScore(['abaaa', 'aacaa'])
	bobScore = calScore(['abc', 'babc', 'abc'])

	# print(aliceScore, bobScore)

	ratio = aliceScore / bobScore

	if ratio > 10000000:
		print("Infinity")
	else:
		print(ratio)
	
	


