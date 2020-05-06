# Question​ : Given a list of packages that need to be built and the dependencies for each 
# package, determine a valid order in which to build the packages.

from queue import Queue

def topo(graph):
	indegree = [0]*len(graph)

	for k,v in graph.items():
		for e in v:
			indegree[e] += 1

	# print("indegree", indegree)
	q = Queue()

	for i in range(len(indegree)):
		if indegree[i]==0:
			q.put(i)
	# print(q.get_nowait())
	# return
	ans = []

	while q.qsize() > 0:
		# print("queue")
		p=q.get_nowait()
		ans.append(p)

		for e in graph[p]:
			indegree[e] -= 1
			if indegree[e] == 0:
				q.put(e)
	# print("ans", ans)
	return ans


graph = {
	0: [],
	1: [0],
	2: [0],
	3: [1,2],
	4: [3]
}

def printRev(arr, i):
	if i+1>len(arr):
		# print("\n")
		return
	else:
		printRev(arr,i+1)
		print(arr[i],end=" ")

# We get a stack of answer
revAns= topo(graph)

# Reversing it to have the answer
printRev(revAns, 0)