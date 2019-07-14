#Depth first search
# My first attempt

#Adjacency matrix
myGraph = {}
myGraph['a'] = ['b', 'c']
myGraph['b'] = ['d', 'e']
myGraph['c'] = ['f', 'g']
myGraph['d'] = []
myGraph['e'] = ['h']
myGraph['f'] = []
myGraph['g'] = []
myGraph['h'] = []

discoveredList = [0] * len(myGraph)
print(discoveredList)
def dfs(myGraph,startVertex):
	Q = []
	discoveredList[ord(startVertex) - 97] = 1
	Q.append(startVertex)
	while Q:
		#print("Q")
		v = Q.pop()
		print(v, end=" ")
		for i in myGraph[v]:
			#print(i)
			if discoveredList[ord(i) -97] == 0:
				Q.append(i)
				discoveredList[ord(i) - 97] = 1
				
		print(discoveredList)


dfs(myGraph,'a')