# Question​ : Given a binary tree, write a function to determine whether the tree is balanced
# @@ Balanced means having all roots have same height

#  For Node Object
class Node():
	def __init__(self,left,right, value):
		self.left = left
		self.right = right
		self.value = value

# constructing binary tree
# eight = Node(None, None, 8)
four = Node(None,None, 4)
five = Node(None,None, 5)
six = Node(None,None, 6)
two = Node(four, five, 2)
three = Node(six, None, 3)
one = Node(two, three, 1)

# Travesrsing till root till we get to the top again
# And comparing once we are about to be on the top
def trav(root, realRoot):
	if root is None:
		return -1

	x = trav(root.left, realRoot)
	y = trav(root.right, realRoot)
	
	if root is realRoot:
		if x!=y:
			return False
		else:
			return True
	return max(x,y)+1

print(trav(one,one))
