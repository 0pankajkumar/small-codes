'''
Question​ : Given a tree, write a function to find the length of the longest branch of nodes
in increasing consecutive order.
'''

class Node():
	def __init__(self,left,right, value):
		self.left = left
		self.right = right
		self.value = value

def longestCon(root, now):
	if root is None:
		return 0
	if root.value == now+1:
		return max(1+longestCon(root.left, root.value), 1+longestCon(root.right, root.value))
	else:
		return 0

# Constructing tree of two children type
one1 = Node(None, None, 1)
two1 = Node(None, None, 2)
one2 = Node(None, None, 1)
three1 = Node(None, None, 3)

one3 = Node(one1, two1, 1)
two2 = Node(one2, three1, 2)

zero1 = Node(one3, two2, 0)

ans = longestCon(zero1, zero1.value-1)
print(ans)