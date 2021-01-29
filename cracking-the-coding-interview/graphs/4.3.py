"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).

        0
      1  2
    3  4 5 6
"""
# import sys 
# sys.stdin = open('input.txt', 'r')  
# sys.stdout = open('output.txt', 'w') 
from collections import deque

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

class LinkedNode(object):
	"""docstring for LinkedNode"""
	def __init__(self, current):
		super(LinkedNode, self).__init__()
		self.current = current
		self.next = None
		

def makeBST(array, start, end):
	if end < start:
		return

	mid = (start + end) // 2

	n = Node(None, None, array[mid])

	n.left = makeBST(array, start, mid-1)
	n.right = makeBST(array, mid+1, end)

	return n

def getStartingOFEachLevel(root, arr):
	if root is None:
		return

	if root.left is not None:
		getStartingOFEachLevel(root.left, arr)
		arr.append(root.value)
		return arr
	else:
		return arr.append(root.value)

def getBFS(root):
	"""Doing a dfs type traversal"""
	if not root:
		return
	queue = deque()
	queue.append(root)
	ans = list()

	while root:
		if len(queue) > 0:
			root = queue.popleft()
		else:
			break

		# print(root.value, end=" ")
		ans.append(root.value)
		if root.left is not None:
			queue.append(root.left)
		if root.right is not None:
			queue.append(root.right)

	return ans

		
def makeDepthLinkedList(root):
	startingsOfDepth = getStartingOFEachLevel(root, list())
	bfsSequence = getBFS(root)

	listOfLinkedLists = list()
	current = None

	for ele in bfsSequence:
		if ele in startingsOfDepth:
			current = LinkedNode(ele)
			listOfLinkedLists.append(current)
		else:
			current.next = LinkedNode(ele)
			current = current.next

	# Printing to see the linked list
	for l in listOfLinkedLists:
		print(l.current, end=" ")
		while l.next:
			print(l.next.current, end=" ")
			l = l.next




newRoot = makeBST([0,1,2,3,4,5,6], 0, 6)

# printTree(newRoot)

# print(getStartingOFEachLevel(newRoot, list()))

makeDepthLinkedList(newRoot)

