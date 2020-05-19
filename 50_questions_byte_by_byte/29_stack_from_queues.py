'''
Question​ : Implement a LIFO stack with basic functionality (push and pop) using FIFO
queues to store the data.
'''

from queue import Queue

class StackFromQueues():
	def __init__(self):
		self.q1 = Queue()
		self.q2 = Queue()
		self.size = 0
		# q1 will be default container holding all elements at a time
		# q2 will be auxillary

	def push_back(self, ele):
		self.q1.put_nowait(ele)
		self.size += 1
		return True

	def pop(self):
		q1 = self.q1
		q2 = self.q2
		while q1.qsize() > 1:
			t = q1.get_nowait()
			q2.put_nowait(t)
		if q1.qsize() > 0:
			ans = q1.get_nowait()
		else:
			ans = None

		self.q1 = q2
		self.q2 = Queue()
		return ans


s = StackFromQueues()
s.push_back(1)
s.push_back(2)
s.push_back(3)
s.push_back(4)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

