class myQueue:
	def __init__(self, val):
		# Our queue will be in this list
		self.qu = list()
		if val is not None:
			self.qu.append(val)

	# Enqueue in Python
	def enq(self, val):
		self.qu.append(val)

	# Dequeue in python
	def dq(self):
		return self.qu.pop(0)

	def vu(self):
		print(self.qu)

qu1 = myQueue(0)

qu1.enq(1)
print("Queue is now")
qu1.vu()
print()

qu1.enq(2)
print("Queue is now")
qu1.vu()
print()

qu1.enq(3)
print("Queue is now")
qu1.vu()
print()

print("Before dqueuing")
qu1.vu()
print()

print("dqueued this")
print(qu1.dq())
print()

print("After dequeing")
qu1.vu()
