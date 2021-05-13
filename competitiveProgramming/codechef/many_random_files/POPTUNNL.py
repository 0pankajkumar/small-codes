# your code goes here
import sys, pprint
sys.stdin = open('input.txt', 'r')


graph = dict()

def dfs(myGraph,startVertex):
	Q = []
	



for _ in range(int(input())):
	n, k = map(int, input().split())
	box = list()
	
	for i in range(n):
		box.append(input())

	
	for i in range(n):
		if i not in graph:
			graph[i] = list()

		for j in range(n):
			if box[i][j] == '1':
				graph[i].append(j)
		

	
	# print(graph)

	# discoveredList = [0] * len(myGraph)

	# Traverse through graph & reach from first item to last quickly, the moment you reach, break
	# Condition: If you are looking to jump from node '1' to '3', you can't jump if you don't have a capacity 2 ('3'-'1' = 2)
	# 			so respect capacity
	# 
