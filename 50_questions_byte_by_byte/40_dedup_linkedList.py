# Question​ : Given an unsorted linked list, write a function to remove all the duplicates.

class Node(object):
	"""docstring for Node"""
	def __init__(self, value, nextt):
		super(Node, self).__init__()
		self.value = value
		self.nextt = nextt


# Set based approach to identify duplicates
def dedup(start):
	bank = set()

	prev = start
	while start:
		if start.value not in bank:
			bank.add(start.value)
			prev = start
			start = start.nextt
		else:
			if start.nextt:
				prev.nextt = start.nextt
				start = start.nextt
				start.nextt = None
			else:
				prev.nextt = None
				start = None


# Creating linked list
one1 = Node(1,None)
two1 = Node(2,one1)
three1 = Node(3,two1)
two2 = Node(2,three1)
one1 = Node(1,two2)

print("Before removing duplicates")
t = one1
while t:
	print(t.value, end=" ")
	t = t.nextt
print("\n")

# Invoking the function to remove duplicates
dedup(one1)

print("After removing duplicates")
t = one1
while t:
	print(t.value, end=" ")
	t = t.nextt
print()
