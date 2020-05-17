'''
Question​ : Given a tree, write a function to convert it into a circular doubly linked list from
left to right by only modifying the existing pointers
'''

class Node():
	def __init__(self,left,right, value):
		self.left = left
		self.right = right
		self.value = value

def helper(root):
	l = root.left
	r = root.right

	if l and r is None:
		return None, None

	l.left = None
	l.right = root

	r.left = root
	r.right = None

	return l,r

def tree2DLL(root):
	if root is None:
		return None, None

	a,b = tree2DLL(root.left)
	c,d = tree2DLL(root.right)

	l1,l2,r1,r2 = [None]*4
	if a and b is None:
		l1, r1 = helper(root)
	if c and d is None:
		l2, r2 = helper(root)
	if a and b and c and d is not None:
		b.right = root
		root.left = b

		root.right = c
		c.left = root

		return a,d

	r1.right = l2
	l2.left = r2
	return l1, r2


# Constructing tree of two children type
four = Node(None,None, 4)
five = Node(None,None, 5)
six = Node(None,None, 6)
seven = Node(None, None, 7)

two = Node(four, five, 2)
three = Node(six, seven, 3)

one = Node(two, three, 1)


x,y = tree2DLL(one)