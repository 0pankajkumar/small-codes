

def createBox(alphabet, isWordStatus):
	box = dict()
	box = {'alphabet': alphabet, 'isWord': isWordStatus, 'nextBoxes': []}
	return box

startBox = createBox(None,False)
startingPoint = startBox

# startBox['nextBoxes'].append(createBox('c', False))
# startBox[-1]['nextBoxes'].append(createBox('a', False))
# startBox[-1]['nextBoxes'][-1]['nextBoxes'].append(createBox('t', False))

def checkInside(li, alpha):
	ind = -1
	found = False
	for l in li:
		ind += 1
		if l['alphabet'] == alpha:
			found = True
	#print(found, ind)
	#Returning found boolean and index where it was found
	return [found, ind]

def insert(startBox, dictionary):
	for di in dictionary:
		i = 0
		startBox = startingPoint
		for w in di:
			if i + 1 == len(di):
				isWordStatus = True
			else:
				isWordStatus = False

			checkResult = checkInside(startBox['nextBoxes'], w)
			if checkResult[0]:
				startBox = startBox['nextBoxes'][checkResult[1]]
			else:
				startBox['nextBoxes'].append(createBox(w, isWordStatus))
				startBox = startBox['nextBoxes'][-1]
			i += 1

def search(box, searchWord):
	found = False
	wordCount = len(searchWord)
	for s in searchWord:
		if wordCount == 2:
			if box['isWord'] == True:
				found = True
		checkResult = checkInside(box['nextBoxes'], s)

		if checkResult[0]:
			box = box['nextBoxes'][checkResult[1]]

		wordCount -= 1

		
	return found





# Inserting a lot of words
insert(startingPoint, ['bus', 'bat', 'bowl', 'cat', 'calf', 'zebra', 'eggs', 'man'])

# Inserting more words
insert(startingPoint, ['xmas', 'xee'])


# To display entire Trie structure
print(startBox)


# To search for a word
# Currently not showing results
print(search(startingPoint, "cat"))

