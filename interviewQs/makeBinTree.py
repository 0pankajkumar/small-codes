# string1 = "7(6(2)(9))(8()(3))"
string = "7(2)(9)"

class Node(object):
	"""docstring for Node"""
	def __init__(self, val, left, right):
		super(Node, self).__init__()
		self.val = val
		self.left = left
		self.right = right

bubble = None
leftIsDone = False

for s in string:
	if s != '(' and s != ')':
		bubble = Node(s, None, None)
	elif s == '(':
		if leftIsDone:
			continue
		bubble.left = s




makeTree(string, 0)
