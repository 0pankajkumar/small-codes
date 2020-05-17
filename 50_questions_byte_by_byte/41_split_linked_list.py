# Question​:Given a linked list, write a function to split the list into two equal halves

class Node(object):
	"""docstring for Node"""
	def __init__(self, value, nextt):
		super(Node, self).__init__()
		self.value = value
		self.nextt = nextt

def printLL(start):
	curr = start
	while curr:
		print(curr.value,end=" ")
		curr = curr.nextt
	print()


def split(start):
	p1 = start
	p2 = start

	part1start = start
	part2start = start

	while p2:
		if p2.nextt:
			if p2.nextt.nextt:
				p2= p2.nextt.nextt
			else:
				part2start = p1.nextt
				p1.nextt = None
				break
		else:
			part2start = p1.nextt
			p1.nextt = None
			break
		p1 = p1.nextt

	return part1start,part2start



# Creating linked list
five = Node(5, None)
four = Node(4, five)
three = Node(3, four)
two = Node(2, three)
one = Node(1, two)

# Getting pointers to splitted linked lists
p1, p2 = split(one)
printLL(p1)
printLL(p2)

