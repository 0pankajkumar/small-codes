'''
Question​ : Given a linked list where each node has two pointers, one to the next node
and one to a random node in the list, clone the linked list
'''

class Node(object):
	"""docstring for Node"""
	def __init__(self, value, nextt, wildNext):
		super(Node, self).__init__()
		self.value = value
		self.nextt= nextt
		self.wildNext = wildNext

# Using an auxiliary space of hashmap 
def copyLL(start):
	if start is None:
		return None

	poin = start.nextt
	copyStart = Node(start.value, None, None)
	t1 = copyStart
	bank = {1:copyStart} # To store objects based on their value to be used as an utility for new linked list creation

	# Creating our new linked list
	while poin:
		t2 = Node(poin.value, poin.nextt, None)
		bank[poin.value] = t2
		t1.nextt = t2
		t1 = t1.nextt
		poin = poin.nextt

	# Creating random linking in our new linked list
	poin = start
	t1 = copyStart
	while poin:
		t1.wildNext = bank[poin.wildNext.value]
		t1 = t1.nextt
		poin = poin.nextt

	# Printing to see whether random links are working
	for i in range(4):
		# if copyStart.wildNext:
		print(copyStart.wildNext.value, end=" ")
		if copyStart.nextt:
			copyStart = copyStart.nextt

	# returing the copied linked list
	return copyStart


# Printing normal next values
def printLL(startt):
	start = startt
	while start:
		print(start.value,end=" ")
		start = start.nextt
	print()

# Printing wild links value
def printLLW(startt):
	start = startt
	while start:
		print(start.wildNext.value,end=" ")
		start = start.nextt
	print()
	

# Using learned method
# Inserting a new node inbetween each
# Then, delinking the inbetween nodes to form an independent LL
def copyLL2(start):

	# Inserting inbetween
	beginning = start
	while beginning:
		newNode = Node(beginning.value, beginning.nextt, None)
		beginning.nextt = newNode
		beginning = newNode.nextt


	# Making the wildNext linking
	beginning = start
	while beginning:
		beginning.nextt.wildNext = beginning.wildNext.nextt
		beginning = beginning.nextt.nextt


	# Decoupling both the LLs
	current = start
	temp = None
	newLL = current
	while current:
		if temp is None:
			temp = current.nextt
			current.nextt = current.nextt.nextt
			newLL = temp
		else:
			temp.nextt = current.nextt
			current.nextt = current.nextt.nextt
			temp = temp.nextt

		current = current.nextt

	# Returning the link to new LL
	return newLL




# Creating linked list
# First simple next linking
four = Node(4, None, None)
three = Node(3, four, None)
two = Node(2, three, None)
one = Node(1, two, None)

# Then, wild linking
one.wildNext = three
two.wildNext = one
three.wildNext = three
four.wildNext = two

# copyLL(one)


lnk = copyLL2(one)

printLL(lnk)
printLLW(lnk)