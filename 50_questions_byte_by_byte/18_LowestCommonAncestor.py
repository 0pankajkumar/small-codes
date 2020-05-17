
class Node():
	def __init__(self,left,right, value):
		self.left = left
		self.right = right
		self.value = value

eight = Node(None, None, 8)
nine = Node(None, None, 9)
ten = Node(None, None, 10)
eleven = Node(None, None, 11)
twelve = Node(None, None, 12)
thirteen = Node(None, None, 13)
fourteen = Node(None, None, 14)
fifteen = Node(None, None, 15)

four = Node(eight,nine, 4)
five = Node(ten,eleven, 5)
six = Node(twelve,thirteen, 6)
seven = Node(fourteen,fifteen, 7)

# four = Node(None,None, 4)
# five = Node(None,None, 5)
# six = Node(None,None, 6)
# seven = Node(None,None, 7)
two = Node(four, five, 2)
three = Node(six, seven, 3)
one = Node(two, three, 1)

def lcs(root,a,b, target):
	if root is None:
		return [False, False] if target == 1 else [True, False]
	
	if target == 1 and root.value == a:
		return [True, False]
	elif target == 2 and root.value == b:
		return [True, True]

	w = lcs(root.left,a,b, target)
	if w[0] is True:
		target = 2
	else:
		w = lcs(root.right,a,b, target)

	x = lcs(root.left,a,b, target)
	if x[0] or w[0] is False:
		return [False, False]
	else:
		return root.value


def dfs(root,a,b,target):
	if root is None:
		return False
	if root.value == target:
		return True
	if dfs(root.left, a,b,target):
		if target == a:
			target = b
			dfs(root.right, a,b,target)
		return True
	else:
		return dfs(root.right, a,b,target)

# An approach using conditional dfs
# target = [target_element, a found status, b found status]
def pseudo(root, a, b, target):
	# If root is None return False statement
	if root is None:
		return False
	elif root.value == target[0]:
		return True 
	if target[1] and target[2] is True:
		target.append(root.value)

	# Check left of root 
	if pseudo(root.left, a, b, target):
		target[0] = b
		target[1] = True
		if target[2]:
			target.append(root.value)
			return True
		else:
			if pseudo(root.right, a, b, target):
				target[2] = True
				target.append(root.value)
				return True
			else:
				return target[1]
	else:
		if pseudo(root.right, a, b, target):
			if target[1] is False:
				target[1] = True
				return True
			else:
				target[2] = True
				target.append(root.value)
				return True
		else:
			return False

	# If a is found, 
		# check right for b
		# If right says b found,
			# root is common ancestor
		# Else
			# return back with say that a was found but still looking for b

	# Check right of root
	# If target is found


# a = 10
# b = 11
# target = [a, False, False]
# pseudo(one, a, b, target)
# print(target)


def depthFirstSearch(root, ele, ans):
	if root is None:
		return False
	elif root.value == ele:
		ans.append(root.value)
		return True

	if depthFirstSearch(root.left, ele, ans):
		ans.append(root.value)
		return True
	elif depthFirstSearch(root.right, ele, ans):
		ans.append(root.value)
		return True

	return False


# Standard approach as learnt online
def getAncestor(root, a, b):
	arr1=[]
	arr2=[]
	depthFirstSearch(root,a,arr1)
	depthFirstSearch(root,b,arr2)

	# print(arr1, arr2)
	# return

	ancestor = None
	found=False
	for x in arr1:
		for y in arr2:
			if x==y:
				ancestor = x
				found=True
				break
		if found:
			break
	print("lowest common ancestor is ",ancestor)

a=14
b=12
getAncestor(one, a, b)