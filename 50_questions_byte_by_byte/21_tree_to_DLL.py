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

def getDLL_helper(root, direction):
	if root.left or root.right is None:
		return None
	t1 = root.left
	t2 = root
	t3 = root.right


	if direction == "right":
		t1.left = root
	else:
		t1.left = None

	t1.right = t2
	t2.left = t1
	t2.right = t3
	t3.left = t2

	if direction == "left":
		t3.right = root
	else:
		t3.right = None

def getDLL(root, direction):
	if root is None or root.left is None or root.right is None:
		return None
	else:
		getDLL_helper(root, "left")
		getDLL_helper(root, "right")

	getDLL(root.left, "left")
	getDLL(root.right, "right")

def concatenate(a,b):
	if a is None:
		return b
	elif b is None:
		return a

	aEnd = a.left
	bEnd = b.left

	a.left = bEnd
	bEnd.right = a
	aEnd.right = b
	b.left = aEnd
	return a

def treeToList(n):
	if n is None:
		return n
	leftList = treeToList(n.left)
	rightList = treeToList(n.right)

	n.left = n
	n.right = n

	n = concatenate(leftList, n)
	n = concatenate(n, rightList)	

	return n

# Constructing tree of two children type
four = Node(None,None, 4)
five = Node(None,None, 5)
six = Node(None,None, 6)
seven = Node(None, None, 7)

two = Node(four, five, 2)
three = Node(six, seven, 3)

one = Node(two, three, 1)


# x,y = tree2DLL(one)

# getDLL(one, "")

ans = treeToList(one)

c=7
while c:
	print(ans.value)
	ans = ans.left
	c-=1

