class MyStack:
	def __init__(self):
		self.stack = []

	def add(self, val):
		self.stack.append(val)

	def popIt(self):
		return self.stack.pop()

	def peekAt(self):
		ele = self.stack
		for i in range(0, len(ele)):
			print(ele[i])

stack1 = MyStack()
stack1.add("Jan")
stack1.add("Feb")
stack1.add("Mar")

print(stack1.popIt())
stack1.peekAt()