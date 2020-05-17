# Question​ : Given a linked list, determine whether it contains a cycle

class Node(object):
	"""docstring for Node"""
	def __init__(self, value, nextt):
		super(Node, self).__init__()
		self.value = value
		self.nextt = nextt
		self.visited = False

# Uses a flag in each node to mark if visited already
def cycleFlagMethod(start):
	conclusion = False
	if start is None:
		return False
	if start.visited is True:
		return True
	else:
		start.visited = True
		conclusion = cycleFlagMethod(start.nextt)
	return conclusion

# Used a double pointer approach
def floydDoublePointer(start):
	slow = start
	fast = start.nextt

	while fast and fast.nextt is not None:
		if slow == fast:
			return True
		else:
			slow = slow.nextt
			fast = fast.nextt.nextt
	return False


'''creating a test Linked list
1 -> 2 -> 3 -> 4 -
     ^           |
     |- - - - - -
'''
prev = Node(1,None)
start = prev
two = None
four = None
for i in range(2,5):
	t = Node(i, None)
	prev.nextt = t
	prev = t

	if i == 2:
		two = t
	if i == 4:
		t.nextt = two
	# t.nextt = None

# Loop for checking Linked list is created or not
'''
for x in range(1,10):
	if start is not None:
		print(start.value, end=" ")
		start = start.nextt
	else:
		print("*", end=" ")
'''


ans = cycleFlagMethod(start)
print("Cycle detected" if ans else "No cycle")

ans = floydDoublePointer(start)
print("Cycle detected" if ans else "No cycle")