'''
Question​ : Write an autocomplete class that returns all dictionary words with a given
prefix
'''

# Trie data structure
class Trie(object):
	"""docstring for Trie"""
	def __init__(self, value):
		super(Trie, self).__init__()
		self.value = value
		self.nextt = dict()
		self.isWord = False


def addWord(start, word):
	root = start
	for i in range(len(word)):
		w = word[i]
		if w not in root.nextt:
			root.nextt[w] = Trie(w)
			root = root.nextt[w]
		else:
			root = root.nextt[w]
		if i+1 == len(word):
			root.isWord = True

def checkWord(start, word):
	root = start
	for i in range(len(word)):
		w = word[i]
		if w not in root.nextt:
			return False
		else:
			root = root.nextt[w]
		if i+1 == len(word) and root.isWord:
			return True

	return False

def getSuffixUtility(root, ans, bigans):
	ans.append(root.value)
	if root.isWord:
		# t = ''.join(ans)
		# bigans.append(t)
		return root.value

	for k,v in root.nextt.items():
		t = getSuffixUtility(v, ans, bigans)
		t1 = ''.join(t)
		bigans.append(t1)
		

def getSuffixWords(start, prefix):

	# Reach there
	root = start
	for i in range(len(prefix)):
		w = prefix[i]
		if w not in root.nextt:
			return False
		else:
			root = root.nextt[w]


	# check for words
	ans = []
	getSuffixUtility(root, [], ans)
	print(ans)
	packedans = []
	for a in ans:
		t = prefix[:-1] + ''.join(a)
		packedans.append(t)
	return packedans
	



root = Trie(".")
addWord(root, "anc")
addWord(root, "anti")
addWord(root, "anty")
addWord(root, "antys")

checkWord(root, "anty")

# for k,v in root.nextt.items():
# 	print(k,end=" ")

ans = getSuffixWords(root, "ant")
print(ans)
		