# Question​ : Implement a binary tree with a method getRandomNode() that returns a
# random node
from random import randrange

class Node():
	def __init__(self,left,right, value):
		self.left = left
		self.right = right
		self.value = value

four = Node(None,None, 4)
five = Node(None,None, 5)
six = Node(None,None, 6)
seven = Node(None,None, 7)
two = Node(four, five, 2)
three = Node(six, seven, 3)
one = Node(two, three, 1)

def inorderRandom(root,manzil, done):
	if not root:
		return
	if done is False and manzil==0:
		manzil = -1
		done = True
	inorderRandom(root.left, manzil-1, done)
	if done is False:
		print(root.value)
		done=True
	inorderRandom(root.right, manzil-1, done)

# inorderRandom(one, randrange(1,7), False)

def inorderRandomHandle(root, lucky):
	count=0
	def inorderRamdom22(root, lucky):
		if root is None:
			return
		count+=1
		inorderRamdom22(root.left, lucky)
		# print("lucky ,count[0]",lucky ,count[0])
		if lucky == count:
			print(root.value)
			# count[0]+=1
		inorderRamdom22(root.right, lucky)
	inorderRamdom22(root, lucky)

# inorderRandomHandle(one, randrange(1,7))

def randomTree(root):
	manzil = randrange(1,7)

	while True:
		manzil-=1
		if manzil==0:
			print(root.value)

'''
This question wanted me to do a iterative traversal instead of recursive
Here is the solution below.
Above codes were my trial
'''


from queue import Queue
def iterative(root):
	lucky = randrange(1,7)
	q = Queue()
	if root is not None:
		q.put_nowait(root)
	else:
		return

	while q.qsize() > 0:
		curr = q.get_nowait()
		lucky -= 1
		if lucky == 0:
			print(curr.value)
			break
		if curr.left is not None:
			q.put_nowait(curr.left)
		if root.right is not None:
			q.put_nowait(curr.right)

iterative(one)

