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
			if len(de) > 1:
				for d in de:
					if d not in path:
						path.append(d)
				return path
			else:
				return path +[de]
	return None

def getAllPaths(g, start, end, path = []):
	path = path + [start]
	if start == end:
		return [path]
	if start not in g:
		return []
	
	for sas in g[start]:
		if sas not in path:
			de = getPath(g, sas, end, path)
		if de:
			if len(de) > 1:
				for d in de:
					if d not in path:
						path.append(d)
				return path
			
	return path

# print(getPath(g, 'a', 'c'))
print(getAllPaths(g, 'a', 'd'))


