'''
Question​:Given a tree, write a function that prints out the nodes of the tree in level
order
'''

from queue import Queue

# Using breadth-first search traversal
# Assuming no cycles
def tree_order(root, graph):
	if not root:
		return

	q = Queue()
	q.put_nowait(root)
	while not q.empty():
		curr = q.get_nowait()
		print(curr, end=" ")

		for e in graph[curr]:
			q.put_nowait(e)
	print()


# Creating adjacency list of graph
graph = {
	1: [2,3],
	2: [4,5],
	3: [6,7],
	4: [],
	5: [],
	6: [],
	7: [],
	9: []
}


tree_order(1, graph)