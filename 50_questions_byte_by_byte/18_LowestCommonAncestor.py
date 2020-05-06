
class Node():
	def __init__(self,left,right, value):
		self.left = left
		self.right = right
		self.value = value

four = Node(None,None, 4)
five = Node(None,None, 5)
six = Node(None,None, 6)
seven = Node(None,None, 7)
two = Node(four, five, 2)
three = Node(six, seven, 3)
one = Node(two, three, 1)

def lcs(root,a,b):
	if lookLeft(root,a):
		



	if lookLeft():
		if lookRight():
			return root
		else:
			return None

	else:
		if lookRight():
			return
		else:
			return None