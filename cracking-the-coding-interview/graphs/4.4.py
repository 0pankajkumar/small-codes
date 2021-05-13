"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.

        0
      1  2
    3  4 5 6
"""

# Prints True if tree is skewed

def printTree(root):
	"""Prints tree in DFS manner"""
	if root is None:
		return

	printTree(root.left)
	print(root.value, end=" ")
	printTree(root.right)

class Node(object):
	"""docstring for Node"""
	def __init__(self, left, right, value):
		super(Node, self).__init__()
		self.value = value
		self.left = None
		self.right = None

def makeBST(array, start, end):
	if end < start:
		return

	mid = (start + end) // 2

	n = Node(None, None, array[mid])

	n.left = makeBST(array, start, mid-1)
	n.right = makeBST(array, mid+1, end)

	return n

def makeSkewBSTHelper(root, array, curr):
	if curr > len(array)-1:
		return

	if array[curr] <= root.value:
		root.left = Node(None, None, array[curr])
		curr += 1
		makeSkewBSTHelper(root.left, array, curr)
	else:
		root.right = Node(None, None, array[curr])
		curr += 1
		makeSkewBSTHelper(root.right, array, curr)


def makeSkewBST(array):
	root = Node(None, None, array[0])
	makeSkewBSTHelper(root, array, 1)
	return root




def getMaxDepthHelper(root, flag):
	if root is None:
		return -1

	x = getMaxDepthHelper(root.left, flag)
	y = getMaxDepthHelper(root.right, flag)

	if abs(x-y) > 1:
		flag[0] = True


	return max(x+1, y+1)

def getMaxDepth(root):
	flag = [False]
	getMaxDepthHelper(root, flag)
	return flag[0]


arr1 = [0,1,2,3,4,5,6,7,88,190,234,999,1009,2345]
arr2 = [0,1,2,3,4,5,6]


# newRoot = makeBST(arr1, 0, len(arr1)-1)
newRoot = makeBST(arr2, 0, len(arr2)-1)

# newRoot = makeSkewBST(arr1)
# newRoot = makeSkewBST(arr2)

# Prints True if tree is skewed
print(getMaxDepth(newRoot))
