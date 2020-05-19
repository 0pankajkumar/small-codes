# Question​ : Given a directed graph, find the shortest path between two nodes if one exists.

'''
Dijistra's algorithm
--------------------

# Get an array per node and mark all positions as infinity
	this is the initial guess of distance from our destination.
# Start with source node and mark distance to itself as 0 and mark as visited
	current node is start node
# Keep looping untill all all nodes are visited
	@ Reach to all nodes possible from current node
	@ If distance marked for that node is less than my distance+the path between us, replace it
	@ Select the min from the list of distances and go to that vertex next
	@ That node is now the next node
# After the loop ends the shortest distance to any node from source nodes can be found from
	the given array

'''

def dijkstra(graph, sou, dest):
	dist = [9999]*(len(graph)+1)
	dist[sou] = 0
	curr = sou
	visitedSet = set()

	while len(visitedSet) < len(graph):
		for e in graph[curr]:
			if dist[curr]+1<dist[e]:
				dist[e] = dist[curr]+1

		mi = dist[0]
		p = 0
		for i in range(0,len(graph)+1):
			if dist[i] <= 0:
				continue
			if dist[i] < mi and i not in visitedSet:
				mi = dist[i]
				p = i
		visitedSet.add(curr)
		curr = p

	return dist[dest]


from queue import Queue
def usingBFS(graph, sou, dest):
	print("entered")
	# if sou or dest is None:
	# 	print(sou, dest)
	# 	print("One of them is None")
	# 	return None

	q = Queue()
	parentBank = dict()
	print("temp vaibales created")

	q.put_nowait(sou)

	print("bfs begins")
	while q.qsize() > 0:
		curr = q.get_nowait()
		for c in graph[curr]:
			if c not in parentBank:
				q.put_nowait(c)
				parentBank[c] = curr
	print("bfs complete")

	ansList = [dest]
	curr = dest
	while curr != sou:
		print("finding using parents")
		if curr in parentBank:
			ansList.append(parentBank[curr])
			curr = parentBank[curr]

	return ansList


def shortestPath22(graph, source, destination, visited, dist):
	int_max = 99999

	if source == destination:
		return dist
	if source not in visited:
		visited.add(source)
	else:
		return int_max

	mini = dist
	for s in graph[source]:
		# For each s ask the magicalFunction of destination distance from s
		if s not in visited:
			thatDistance = shortestPath22(graph, s, destination, visited, dist+1)
			mini = max(mini, thatDistance)

	return mini

def shortestPath(graph, source, destination, visited, dist, ans):
	int_max = 99999

	if source == destination:
		return dist
	if source not in visited:
		visited.add(source)
	else:
		return int_max

	mini = dist
	for s in graph[source]:
		# For each s ask the magicalFunction of destination distance from s
		if s not in visited:
			thatDistance = shortestPath(graph, s, destination, visited, dist+1, ans)
			mini = max(mini, thatDistance)

	return mini


graph = {
	1: [2,3],
	2: [5],
	3: [],
	4: [1,3],
	5: [4]
}

source = 2
destination = 3
ans = list()
# print(shortestPath22(graph, source, destination, set(), 0))
# shortestPath(graph, source, destination, set(), 0, ans)
# print(ans)

# print(dijkstra(graph, source, destination))

ans = usingBFS(graph, source, destination)

print(ans[::-1])