
'''
Question​ : Given a matrix, find the path from top left to bottom right with the greatest
product by moving only down and right.
Solution​ : ​https://www.byte-by-byte.com/matrixproduct/
'''

def maxProduct(mat,i,j, ans):
	# DP based solution
	# Fails to do well with mat2
	if i >= len(mat) or j >= len(mat[0]):
		return ans
	if pk[i][j] is not None:
		return pk[i][j]
	a = maxProduct(mat,i+1,j, ans*mat[i][j])
	pk[i+1][j] = a
	b = maxProduct(mat,i,j+1, ans*mat[i][j])
	pk[i][j+1] = b
	return max(a, b)

def maxProduct1(mat,i,j, ans):
	# Basic recursion
	if i >= len(mat) or j >= len(mat[0]):
		return ans
	a = maxProduct1(mat,i+1,j, ans*mat[i][j])
	b = maxProduct1(mat,i,j+1, ans*mat[i][j])
	return max(a, b)


mat1 = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

mat2 = [
	[-1,2,3],
	[4,5,-6],
	[7,8,9]
]	

pk = [[None for i in range(4)] for j in range(4)]
print(pk)
print(maxProduct1(mat2,0,0, 1))
print(pk)