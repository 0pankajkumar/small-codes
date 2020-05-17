'''
Question​ : Write an autocomplete class that returns all dictionary words with a given
prefix
'''

# Trie data structure
class Trie(object):
	"""docstring for Trie"""
	def __init__(self, value, nextt=dict(), isWord=False):
		super(Trie, self).__init__()
		self.value = value
		self.nextt = nextt
		self.isWord = isWord


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

def getSuffixUtility(root,ans):
	if root.isWord:
		# ans.append("")
		return

	for k,v in root.nextt.items():
		ans.append(k)
		getSuffixUtility(v, ans)

	ans.append(root.value)


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
	getSuffixUtility(root, ans)
	return ans
	



root = Trie(".")
print(root.nextt)
addWord(root, "ant")
print(root.nextt)

# print(root.nextt['a'].nextt['a'].nextt['a'].nextt['a'].nextt['a'].nextt['a'].nextt['a'].nextt['a'])

addWord(root, "anti")
print(root.nextt)
checkWord(root, "anty")

# for k,v in root.nextt.items():
# 	print(k,end=" ")

getSuffixWords(root, "an")
		