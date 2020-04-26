'''
Question​ : Given a boolean matrix, update it so that if any cell is true, all the cells in that
row and column are true.
'''

def zero(mat):
	newMat = [m[:] for m in mat]
	i = 0
	while i < len(mat):
		j = 0
		while j < len(mat[0]):
			if mat[i][j] is True:
				# Horizontally
				for k in range(len(mat[0])):
					newMat[i][k] = True
				for k in range(len(mat)):
					newMat[k][j] = True
				break
			j+=1
		i+=1
	return newMat

# [True, True, True],
# [True, False, False],
# [True, False, False]

# i = 1
# j = 0





mat1 = [
	[True, False, False],
	[False, False, False],
	[False, False, False]
]

mat2 = [
	[False, False, False],
	[False, True, False],
	[False, False, False]
]
print(zero(mat2))
# print(mat2)