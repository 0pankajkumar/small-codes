# Adjacency list approach of making a graph

g = {
	'a':['b', 'c'],
	'b':['c', 'd'],
	'c':['d'],
	'd':['c'],
	'e':['f'],
	'f':['c']
}

def getPath(g, start, end, path = []):
	path = path + [start]
	if start == end:
		return path
	if start not in g:
		return None
	
	for sas in g[start]:
		if sas not in path:
			de = getPath(g, sas, end, path)
		if de:
			return path
	return None

#path = []
print(getPath(g, 'a', 'd'))
#print(path)