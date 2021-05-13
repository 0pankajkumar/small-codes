"""
Build order:
Determine what build order to follow when dependencies are given
"""

graph = {}
projects = ['a', "b", "c", "d", "e", "f"]
dependencies = [("a","d"), ("f","b"), ("b","d"), ("f","a"), ("d","c")]


# Make the graph

for dep in dependencies:
	node = dep[0]
	conn = dep[1]
	if node not in graph:
		graph[node] = [conn]
	else:
		graph[node].append(conn)

print(graph)

def dfs(root, visited):
	if root in visited:
		return

	if root in graph:
		for ele in graph[root]:
			if ele not in visited:
				print(ele)
				dfs(ele, visited)
				visited.add(ele)

dfs("f", set())