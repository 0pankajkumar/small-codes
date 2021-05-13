import sys  
sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')  



# Author : pankaj2kumar@codechef
def problemSolver2(n,stree):
	ascored=0
	bscored=0
	amiss=0
	bmiss=0
	arem=n
	brem=n
	asTurn=True

	for i in range(2*n):
		if ascored > (bscored + brem):
			return i 
		elif bscored > (ascored + arem):
			return i


		if stree[i] == '1':
			if (i+1) % 2 == 0:
				ascored += 1
				arem -= 1
			else:
				bscored += 1
				brem -= 1
		else:
			if (i+1) % 2 == 0:
				amiss += 1
				arem -= 1
			else:
				bmiss += 1
				brem -= 1

	return n*2


def problemSolver1(n,stree):
	ascored=0
	bscored=0
	amiss=0
	bmiss=0
	arem=n
	brem=n
	asTurn=True

	for i in range(2*n):
		if ascored > brem or bscored > arem:
			# print(ascored,brem,bscored,arem)
			if ascored != bscored:
				return i 

		if ascored-bscored > 0:
			if brem < (ascored-bscored):
				return i
		elif bscored-ascored > 0:
			if arem < (bscored-ascored):
				return i

		# if chances remaining is less than goal difference return i


		if stree[i] == '1':
			if (i+1) % 2 == 0:
				ascored += 1
				arem -= 1
			else:
				bscored += 1
				brem -= 1
		else:
			if (i+1) % 2 == 0:
				amiss += 1
				arem -= 1
			else:
				bmiss += 1
				brem -= 1


	return n*2









def inputHandler1():
	for ssss in range(int(input())):
		n = int(input())
		stree = str(input())
		# print(n,stree)
		
		print(problemSolver2(n, stree))


inputHandler1()