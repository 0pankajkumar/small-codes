'''
Question​ : Given a binary search tree, print out the elements of the tree in order without
using recursion	
'''
from queue import LifoQueue

#  For Node Object
class Node():
	def __init__(self,left,right, value):
		self.left = left
		self.right = right
		self.value = value
		self.visited = False

def inorderIterative22(root):
	s = LifoQueue()
	curr = root
	s.put_nowait(curr)

	while curr is not None and s.qsize() != 0:
		s.put_nowait(curr)
		while curr is not None:
			curr = curr.left
		if s.qsize() != 0:
			t = s.get_nowait()
			print(t.value,end=" ")
			curr = t.right

def inorderIterative33(root):
	curr = root
	stack = []
	done = 0

	while True:
		if curr is not None:
			stack.append(curr)
			curr = curr.left

		elif stack:
			curr = stack.pop()
			print(curr.value, end=" ")
			curr = curr.right
		else:
			break
	print()


def inorderIterative(root):
	if root is None:
		return None
	count = 0
	stack = LifoQueue()
	stack.put_nowait(root)
	ans = list()

	while True:
		if root is not None:
			print(root.value,end=" ")
			for i in range(1,3):
				if i==1:
					if root.left is not None:
						stack.put_nowait(root.left)
						print(root.left.value, end=" ")
				else:
					if root.right is not None:
						stack.put_nowait(root.left)
						print(root.right.value, end=" ")

		if stack.qsize() != 0:
			root = stack.get_nowait()
		else:
			break

	# while count <= 7:
		
	# 	if root.left is not None:
	# 		stack.put_nowait(root.left)
	# 		ans.append(root.left.value)
	# 	if root is not None:
	# 		stack.put_nowait(root)
	# 		ans.append(root.value)
	# 	else:
	# 		ans.append(root.value)
	# 	if root.right is not None:
	# 		stack.put_nowait(root.right.value)
	# 		ans.append(root.right.value)

	# 	count += 1

	# print(ans)



	# while count <= 7 :
	# 	if root.left is not None and root.left.visited is False:
	# 		root = root.left
	# 		stack.put_nowait(root)
	# 	elif root.right is not None and root.right.visited is False:
	# 		root = root.right
	# 		stack.put_nowait(root)
	# 	else:
	# 		print(root.value,end=" ")
	# 		root.visited = True
	# 		count += 1
	# 		# return stack
	# 		if stack.qsize() != 0:
	# 			root = stack.get_nowait()
	# 		else:
	# 			break
	print()




# constructing a good binary search tree
one = Node(None, None, 1)
three = Node(None, None, 3)
six = Node(None, None, 6)
eight= Node(None, None, 8)
two = Node(one, three, 2)
seven = Node(six, eight, 7)
five = Node(two, seven, 5)



inorderIterative33(five)
