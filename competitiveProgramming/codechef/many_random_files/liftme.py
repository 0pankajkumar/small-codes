'''
Author : pankaj2kumar@codechef
'''
import sys  
sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')  


def problemSolver1():
	print()

def inputHandler1():
	for ssss in range(int(input())):
		n,q = map(int, input().split())
		first = True
		dold=None
		fold=None
		ans=0
		for sss in range(q):
			f,d = map(int, input().split())
			# print("f,d",f,d)
			if first:
				ans += f
				ans += abs(d-f) 
				first = False
			else:
				# print("abs(dold-f)",abs(dold-f))
				ans += abs(dold-f)
				ans += abs(d-f)
			dold=d 
			fold=f 

		print(ans)


		# problemSolver1()


inputHandler1()