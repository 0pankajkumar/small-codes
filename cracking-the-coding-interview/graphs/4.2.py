"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo-rithm to create a binary search tree with minimal height. 


        0
      1  2
    3  4 5 6
"""
import sys 
sys.stdin = open('input.txt', 'r')  
# sys.stdout = open('output.txt', 'w') 

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







newRoot = makeBST([0,1,2,3,4,5,6], 0, 6)

printTree(newRoot)