# https://www.codechef.com/DI15R080/problems/GUESSWAY
from pptree import *

class myTreeNode():
	def __init__(self,test):
		self.left = None
		self.right = None
		self.visited = False
		self.isExit = False
		self.test = test
		self.isLeaf = False


def perfectBinaryTree(root, height):
	global leafCount
	height += 1
	if(height < limit):
		number = 5
		root.left = myTreeNode(number)
		root.right = myTreeNode(number)
		number = 5
		if leafCount == 1:
			root.isExit = True
		perfectBinaryTree(root.left, height)
		perfectBinaryTree(root.right, height)
	else:
		leafCount -= 1
		root.isLeaf = True

def Inorder(root):
	if root:
		Inorder(root.left)
		print(f"{root.test}-{root.isLeaf}", end=" ")
		Inorder(root.right)


limit = 4
number = 0
leafCount = 3

root = myTreeNode(0)
perfectBinaryTree(root, 0)
Inorder(root)


# cases = int(input())

# for cas in range(cases):
# 	h,n = map(int, input().split())
