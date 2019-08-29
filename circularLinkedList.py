

class LinkedList():
	def __init__(self,element):
		self.data = element
		self.next = None


class CircularLinkedList():
	def __init__(self, node):
		self.node = node

	def enque(self, head, node):
		if head is None:
			head = node
			head.next = head
		else:
			start = head
			while(head.next is not None and head.next is not start):
				head = head.next
				# print(head.data)
			head.next = node
			# head = head.next
			head.next.next = start

	def view(self, head):
		start = head
		while(head is not None):
			
			print(head.data)
			head = head.next
			if head.next is start:
				break

head = LinkedList(0)
n = CircularLinkedList(head)
n.enque(head, LinkedList(1))
n.enque(head, LinkedList(2))
n.enque(head, LinkedList(3))
n.enque(head, LinkedList(4))

n.view(head)

