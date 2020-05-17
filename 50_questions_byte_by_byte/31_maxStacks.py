'''
Question​ : Implement a LIFO stack that has a push(), pop(), and max() function, where
max() returns the maximum value in the stack. All of these functions should run in O(1)
time
'''
from queue import LifoQueue
class Box (object):
	"""docstring for Box """
	def __init__(self, value, nextMax):
		super(Box , self).__init__()
		self.value = value
		self.nextMax = nextMax
		
class Stack():
	def __init__(self):
		self.container = LifoQueue()

	def push(self, ele):
		e = None
		if self.container.qsize() == 0:
			e = Box(ele, ele)
			self.container.put_nowait(e)
		else:
			# get the top element
			# if its nextMax < current element, 
			# nextMax of curr is the same element otherwise its of previous elememt
			# Put it back
			t = self.container.get_nowait()
			maxi = None
			if t.nextMax > ele:
				maxi = t.nextMax
			else:
				maxi = ele
			self.container.put_nowait(t)

			e = Box(ele, maxi)
			self.container.put_nowait(e)

	def pop(self):
		ele = self.container.get_nowait()
		return ele.value
		

	def max(self):
		t = self.container.get_nowait()
		ans = t.nextMax
		self.container.put_nowait(t)
		return ans


myStack = Stack()
myStack.push(1)
print(myStack.max())
myStack.push(2)
print(myStack.max())
myStack.push(1)
print(myStack.max())
print(myStack.pop())
print(myStack.max())
print(myStack.pop())
print(myStack.max())





















'''
from queue import LifoQueue
import heapq

class Box():
	def __inti__(self, value, prevMax):
		self.value = value
		self.prevMax = prevMax

class Stack():
	def __init__(self):
		self.container = LifoQueue()
		self.uriaHeap = list()

	def push(self, ele):
		self.container.put_nowait(ele)
		heapq.heappush(self.uriaHeap, ele)

	def pop(self):
		ele = self.container.get_nowait()
		return ele

	def max(self):
		return self.uriaHeap[-1]



myStack = Stack()
myStack.push(1)
print(myStack.max())
myStack.push(2)
print(myStack.max())
myStack.push(1)
print(myStack.max())
print(heapify(myStack.uriaHeap))
# print(myStack.pop())
# print(myStack.max())
# print(myStack.pop())
# print(myStack.max())
'''