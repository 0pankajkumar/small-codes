"""
Implementing my own hashtable
"""

class Container(object):
	"""docstring for container"""
	def __init__(self, key, val, nex=None):
		self.key = key
		self.val = val
		self.next = nex


class Linked(object):
	"""docstring for linked"""
	def __init__(self, start):
		self.start = start

	def insert(self, key, val):
		now = self.start
		while now:
			if now.key == key:
				now.val = val
				return
			else:
				now = now.next
		now.next = Container(key, val, None)

	def find(self, key):
		now = self.start
		while now:
			if now.key == key:
				return now.val
			now = now.next
		return False


class HashTable(object):
	"""docstring for HashTable"""
	def __init__(self):
		self.table = [None for i in range(10)]

	def store(self, key, val):
		location = hash(key) % 10
		if self.table[location] is None:
			self.table[location] = Linked(Container(key, val))
		else:
			self.table[location].insert(key, val)

	def fetch(self, key):
		location = hash(key) % 10
		if self.table[location] is None:
			return False
		else:
			return self.table[location].find(key)


h = HashTable()
h.store('a', 'aa')
h.store('b', 'bb')
h.store('e', 'ee')
print(h.fetch('a'))
print(h.fetch('b'))
print(h.fetch('e'))