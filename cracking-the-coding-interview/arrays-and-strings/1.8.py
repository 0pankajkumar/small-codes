def make_row_column_zero(x, y, matrix):
    m = len(matrix)
    n = len(matrix[0])

    i = x
    j = y
    while i >= 0 and j >=0 and i < m and j < n:
        matrix[i][j] = 0
        i -= 1

    i = x
    j = y
    while i >= 0 and j >=0 and i < m and j < n:
        matrix[i][j] = 0
        j -= 1

    i = x
    j = y
    while i >= 0 and j >=0 and i < m and j < n:
        matrix[i][j] = 0
        i += 1

    i = x
    j = y
    while i >= 0 and j >=0 and i < m and j < n:
        matrix[i][j] = 0
        j += 1


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

make_row_column_zero(2, 1, matrix)
print(matrix)