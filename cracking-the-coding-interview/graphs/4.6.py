"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.


The code doesn't runs actually
It's a pseudo code to demonstrate

"""

def findInOrderSuccessor(root, element):
	if root or element is None:
		return
	if root.value == element:
		return element

	# Search the element starting from root using any tree traversal
	elementNode = searchTheElement(root, element)
	notFound = True

	while notFound:
		if elementNode.right is None:
			# If you are coming up from the left side
			if elementNode.parent.left.value == elementNode.value:
				elementNode = elementNode.parent
				notFound = False
				break
			else:
				# Traversing upside
				while notFound:
					if elementNode.parent.value < element:
						elementNode = elementNode.parent
					else:
						elementNode = elementNode.parent
						notFound = False
						break

		else:
			elementNode = elementNode.right
			# Go towards the left now
			while notFound:
				if elementNode.left is None:
					notFound = False
					break
				else:
					elementNode = elementNode.left


	print(elementNode.value)







findInOrderSuccessor(None, None)