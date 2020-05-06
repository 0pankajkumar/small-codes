'''
Question​ : Given 2 sorted arrays, A and B, where A is long enough to hold the contents of
A and B, write a function to copy the contents of B into A without using any buffer or
additional memory
'''

def pushArray(A,id):
	t=A[id]
	for i in range(id,len(A)-id):
		if i+1<len(A):
			t = A[i+1]
			A[i+1] = A[i]

def pushArray2(A,id):
	for i in range(len(A)-1, id-1, -1):
		A[i] = A[i-1]

def purifyA(A):
	# Makes 0's at the end as None since they represent empty spaces only
	for i in range(len(A)-1,-1,-1):
		if A[i] == 0:
			A[i] = None
		else:
			break

def mergeTwoArrays(A,B):
	i=0; j=0
	purifyA(A)
	while i<len(A) and j<len(B):
		if A[i] is None:
			A[i] = B[j]
			j+=1
		elif A[i] > B[j]:
			pushArray2(A,i)
			A[i] = B[j]
			# break
			j+=1
		i+=1
	print(i,j)

A = [1,3,5,0,0,0,0]
B = [2,4,6,7]

mergeTwoArrays(A,B)
print(A,B)