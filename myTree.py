# A simple tree,
# My first tree in python

class myTreeNode():
	def __init__(self,val):
		self.left = None
		self.right = None
		self.val = val

def Inorder(root):
	if root:
		Inorder(root.left)
		print(root.val, end=" ")
		Inorder(root.right)

def Preorder(root):
	if root:
		print(root.val, end=" ")
		Preorder(root.left)
		Preorder(root.right)

def Postorder(root):
	if root:
		Postorder(root.left)
		Postorder(root.right)
		print(root.val, end=" ")

root = myTreeNode(1)
root.left = myTreeNode(2)
root.right = myTreeNode(3)
root.left.left = myTreeNode(4)
root.left.right = myTreeNode(5)

print("Inorder")
Inorder(root)
print("\n\nPreorder")
Preorder(root)
print("\n\nPostorder")
Postorder(root)