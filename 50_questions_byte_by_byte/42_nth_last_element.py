'''
Question​:Given a linked list, and an input n, write a function that returns the nth-to-last
element of the linked list.
'''

class Node(object):
	"""docstring for Node"""
	def __init__(self, value, nextt):
		super(Node, self).__init__()
		self.value = value
		self.nextt = nextt
		self.revPosition = None


def nthLast(start, n):
	if not start:
		return -1,False,None
	else:
		temp = nthLast(start.nextt, n)
		# print(temp)
		if temp[1]:
			return temp[0],True,temp[2]
		else:
			count = 1 + temp[0]
		if n == count:
			return count,True,start.value
		else:
			return count, False, temp[2]






# Creating linked list
five = Node(5, None)
four = Node(4, five)
three = Node(3, four)
two = Node(2, three)
one = Node(1, two)

n = 5
ans = nthLast(one, n)
print(ans[2])
