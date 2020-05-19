# Question​ : Given a stack, sort the elements in the stack using one additional stack

class Stack():
	def __init__(self):
		self.container = list()

	def empty(self):
		if len(self.container) == 0:
			return True
		else:
			return False

	def length(self):
		return len(self.container)

	def top(self):
		if not self.empty():
			return self.container[-1]
		else:
			return None

	def push_back(self, ele):
		if ele is not None:
			self.container.append(ele)
			# print(f"Added {ele} to stack")

	def pop(self):
		if not self.empty():
			t = self.container[-1]
			del self.container[-1]
			return t
		else:
			return None




def sortStack(myStack):
	auxStack = Stack()
	auxStack.push_back(myStack.pop())

	while not myStack.empty():
		t = myStack.pop()


		while not auxStack.empty() and t < auxStack.top():
			myStack.push_back(auxStack.pop())
		auxStack.push_back(t)


		# if auxStack.top():
		# 	if auxStack.top() < t:
		# 		t2 = auxStack.pop()
		# 		myStack.push_back(t2)
		# 		auxStack.push_back(t)

		# 		c=0
		# 		while auxStack.top() < t2:
		# 			c+=1
		# 			myStack.push_back(auxStack.pop())

		# 		myStack.push_back(t2)

		# 		while c:
		# 			auxStack.push_back(myStack.pop())
		# 			c-=1
		# 	else:
		# 		auxStack.push_back(t)
	myStack.container = auxStack.container
	print("aux",auxStack.container)


myStack = Stack()
myStack.push_back(12)
myStack.push_back(4)
myStack.push_back(6)
myStack.push_back(1)

print("before",myStack.container)
sortStack(myStack)
print("after",myStack.container)