'''
Author : pankaj2kumar@codechef
'''
import sys  
sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')  


def problemSolver1(stree):
	count = 0
	ans = 0
	for i in range(len(stree)):
		if stree[i] == '<':
			count += 1
		elif stree[i] == '>':
			if count <= 0:
				break
			count -= 1
		if count == 0:
			ans = (i+1)

	return ans
	

def inputHandler1():
	for ssss in range(int(input())):
		stree = input()
		print(problemSolver1(stree))


inputHandler1()