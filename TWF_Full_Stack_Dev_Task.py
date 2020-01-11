# The backend logic

# Modelling the graph
class edge(object):
	def __init__(self, start, end, weight):
		self.start = start
		self.end = end
		self.weight = weight

p = edge('1', '2', 4)
q = edge('1', 'h', 3)
r = edge('3', 'h', 2)
s = edge('2', '3', 3)
t = edge('2', 'h', 2.5)

g2 = {
	'1': [p, q],
	'2': [p, t, s],
	'3': [r, s],
	'h': [q, t, r]
}

g = {
	'1': {'2':4, 'h':3},
	'2': {'1':4, 'h':2.5, '3':3},
	'3': {'2':3, 'h':2},
	'h': {'1':3, '2':2.5, '3':2}
}

def getDistance(g, kk, k, v):
	return v




def getPath(g, kk, k, v, total=0):
	# We have reached home
	# if edge.end == 'h':
	# 	return the total sum
	# else:
	# 	getPath(add the distance, new edge = edge.end)

	# g[kk][k] = v
	if v == 'h':
		total += getDistance(g, kk, k, v)
		return total
	else:
		total += getDistance(g, kk, k, v)
		getPath(g, kk, k, v, total)

		

def allPathHelper(g):
	# for each vertex in graph
	# 	get each vertex get to each path & start the journey

	for kk, vv in g.items():
		for k,v in g[kk].items():
			print(kk, k, v, type(v))
			total = 0 
			total = getPath(g, kk, k, v)
			print(total)




allPathHelper(g)

































# sum = 0
# for each path
# 	for each distance
# 		there will be a cost
# 		sum of that cost
# if sum < minGlobalCost:
# 	minGlobalCost = sum