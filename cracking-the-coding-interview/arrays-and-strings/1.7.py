"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
"""

matrix = [[1, 2, 3, 4],
		  [5, 6, 7, 8],
		  [9, 10,11,12],
		  [13,14,15,16]
]

rev = [
	[13, 9, 5, 1],
	[14,10, 6, 2],
	[15,11, 7, 3],
	[16,12, 8, 4]
]


def circularSwap(x, y, gap, direction, theNumber):
	# print(x,y)
	if direction == 1:
		y += gap
		circularSwap(x, y, gap, 2, matrix[x][y])
		matrix[x][y] = theNumber
	elif direction == 2:
		x += gap
		circularSwap(x, y, gap, 3, matrix[x][y])
		matrix[x][y] = theNumber
	elif direction == 3:
		y -= gap
		circularSwap(x, y, gap, 4, matrix[x][y])
		matrix[x][y] = theNumber
	elif direction == 4:
		x -= gap
		# y -= gap
		circularSwap(x, y, gap, 5, matrix[x][y])
		matrix[x][y] = theNumber
	else:
		matrix[x][y] = theNumber 

def rotate(matrix):
	n = len(matrix)
	start = 0
	gap = 3
	for i in range(n//2):
		for j in range(start,n//2):
			# print(start,j)
			circularSwap(start, start, gap, 1, matrix[start][j])
		gap -= 2 
		start += 1


print(matrix)
circularSwap(0, 1, 2, 1, matrix[0][0])

# rotate(matrix)

print(rev)
print(matrix)