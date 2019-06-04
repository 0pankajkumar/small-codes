class LinkedList:
	def __init__(self,val):
		self.val = val
		self.next = None

	def traverse(self):
		node = self
		while node != None:
			print(node.val, end=" ")
			node = node.next


element1 = LinkedList(1)
element2 = LinkedList(2)
element3 = LinkedList(3)

element1.next = element2
element2.next = element3

element1.traverse()