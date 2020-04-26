'''
Author : pankaj2kumar@codechef
'''
import sys  
sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')  

def problemSolver3(n,arr):
	maxi = max(arr)
	startFound = False
	lorry = []
	start = 0
	end = 0
	for i in range(n):
		if arr[i] == maxi:
			if startFound is True:
				end = i
				lorry.append(end-start)
				startFound = False
			else:
				startFound = True
				start = i

	print(lorry)

	ans = 0
	for l in lorry:
		ans += max(l - (n/2) + 1, 0)
	print(int(ans))

def problemSolver2(n,arr):
	lmax = arr[0]
	pos = None
	for i in range(int(n/2+1)):
		if arr[i] >= lmax:
			lmax = arr[i]
			pos = i
	if pos is None:
		a = 0
	else:
		a = (n - pos) -((n/2)-pos)



	lmax2 = arr[int(n/2)]
	pos = None
	for i in range(int(n/2),n):
		if arr[i] >= lmax2:
			lmax2 = arr[i]
			pos = i
	if pos is None:
		b = 0
	else:
		b = n - pos - 1

	print(int(a-b))


def problemSolver1(n,arr):
	#find maximum's position
	lmax = arr[0]
	pos = 0
	for i in range(n):
		if arr[i] >= lmax:
			lmax = arr[i]
			pos = i

	a=0
	b=0
	# If it's in 1st half
	if pos < (n/2):
		ans = (n - pos) -((n/2)-pos)
		a = ans
	# If it's in second half
	else:
		ans = n - pos - 1
		b = ans
	print(a-b)

	# print(int(ans))





def inputHandler1():
	for ssss in range(int(input())):
		n = int(input())
		arr = list(map(int, input().split()))

		problemSolver3(n,arr)


inputHandler1()