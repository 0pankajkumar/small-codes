import sys 
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w') 

from collections import deque

tree = dict()
visited = set()
pathToA = deque()
pathToB = deque()
foundA = False

def dfs_findPath(ele, toFind, pathDeque):
	global foundA

	if ele in visited or foundA:
		return

	visited.add(ele)

	if ele == toFind:
		foundA = True
		pathDeque.append(ele)

	if not foundA:
		pathDeque.append(ele)

	for a in tree[ele]:
		if a not in visited:
			dfs_findPath(a, toFind, pathDeque)

			if not foundA:
				pathDeque.pop()



 #     1
 #   2   3
 # 4  5 6  7





def addToTree(a, b):
	if a in tree:
		tree[a].append(b)
	else:
		tree[a] = [b]

	if b in tree:
		tree[b].append(a)
	else:
		tree[b] = [a]
	# print(tree)

def solve():
	n = int(input())

	for i in range(n-1):
		rw= list(map(int, input().split()))
		# continue
		a = rw[0]
		b = rw[1]
		addToTree(a, b)

	# Find Path to A
	dfs_findPath(1, 4, pathToA)
	print("pathToA", pathToA)

	global foundA, visited
	# print("foundA is", foundA)
	foundA = False
	visited = set()

	# Find Path to B
	dfs_findPath(1, 7, pathToB)
	print("pathToB", pathToB)

	# Finding the path A-B
	i = -1
	while i < n:
		i += 1

		if pathToA[i] != pathToB[i]:
			i -= 1
			break

	for i in range(len(pathToA)-1, i-1, -1):
		print(pathToA[i], end=" -> ")

	for i in range(i+1, len(pathToB)):
		print(pathToB[i], end=" -> ")


for testcases in range(int(input())):
	solve()

