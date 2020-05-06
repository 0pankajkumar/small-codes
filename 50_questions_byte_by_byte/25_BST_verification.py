# Question​ : Given a binary tree, write a function to test if the tree is a 
# binary search tree

#  For Node Object
class Node():
	def __init__(self,left,right, value):
		self.left = left
		self.right = right
		self.value = value

def bst_verify(root):
	if root is None:
		return True

	x = bst_verify(root.left)
	y = bst_verify(root.right)

	if x and y is True:
		mark1=False
		mark2=False
		if root.left:
			if root.left.value <= root.value:
				mark1=True
		else:
			mark1=True

		if root.right:
			if root.right.value >= root.value:
				mark2= True
		else:
			mark2=True
		if mark1 and mark2 is True:
			return True
	
	return False


# constructing a good binary search tree
one = Node(None, None, 1)
three = Node(None, None, 3)
six = Node(None, None, 6)
eight= Node(None, None, 8)
two = Node(one, three, 2)
seven = Node(six, eight, 7)
five = Node(two, seven, 5)

# constructing a bad binary search tree
one_bad = Node(None, None, 1)
three_bad = Node(None, None, 3)
six_bad = Node(None, None, 6)
four_bad = Node(None, None, 4)
two_bad = Node(one_bad, three_bad, 2)
seven_bad = Node(six_bad, four_bad, 7)
five_bad = Node(two_bad, seven_bad, 5)


print(bst_verify(five))