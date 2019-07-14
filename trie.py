class element(object):
	"""docstring for element"""
	def __init__(self, word, flag):
		self.word = word
		self.isWord = flag
		self.next = []

headElement = element(None, False)
startElement = headElement

def initFun(extFile,startElement):
	for ex in extFile:
		hElement = startElement
		isWordFlag = False
		wordAlreadyExist = None
		for i in range(len(ex)):
			if i == len(ex) - 1:
				isWordFlag = True
			else:
				isWordFlag = False
			elementJustCreated = element(ex[i], isWordFlag)
			index = 0
			for h in hElement.next:
				if h.word == ex[i]:
					wordAlreadyExist = True
				else:
					wordAlreadyExist = False
				index += 1
			if wordAlreadyExist == False:
				hElement.next.append(elementJustCreated)
				hElement = hElement.next[-1]
			else:
				hElement = hElement.next[index]

def search(word):
	elementNotFound = False
	for element in startElement.next:
		if word[0] == element.word:
			element = startElement.next[index(word[0])]
			print("Found it in startElement")
			elementNotFound = False
			break
		else:
			elementNotFound == True

	if elementNotFound == True:
		return False

	for w in word:
		if w == word[-1]:
			if element.isWord == True:
				return True
			else:
				return False

		elementNotFound = False
		index = None
		for i in range(len(element.next)):
			if w == element.next[i]:
				index = i
				break
			else:
				elementNotFound = True
		if elementNotFound == False:
			element = element.next[index]
		else:
			return False

def search2(word, startElement):
	print("Inside search2")
	for ele in startElement.next:
		print(ele.word)
		if word[0] == ele.word:
			print("Z found")
			element = startElement.next.index(word[0])
		else:
			print("Z not found")
			return False
	for w in word:
		ret = searchDeep2(element, w)
		if w == word[-1]:
			if ret[1] == True:
				return True
		if element.next.index(w):
			element = element.next[element.next.index(w)]
		else:
			return False


def searchDeep2(element, wordToSearch):
	if element.word == wordToSearch:
		if element.isWord == True:
			#First flag for alphabet exist
			#Second flag to show word 
			return [True, True]
		else:
			return [True, False]
	else:
		return [False, False]



#Iterating through trie to check whether load has happened
def printAlpha(element):
	print(element.word)
	for ele in element.next:
		printAlpha(ele)
	


initFun(['abc', 'bat', 'zee', 'cat', 'calf', 'zebra', 'eggs', 'man'], startElement)	

printAlpha(startElement)

print(search2('zebra', startElement))
#print(startElement.next[0])